'use strict';

/* Services */


angular.module('bitmart.services', ['ngResource'])

  /* Product resource */
  .factory('Product', function($resource) {
    return $resource('/api/product/:productId', {}, {
      query: {
        method:'GET',
        params: {},
        isArray:true,
        transformResponse: [
          function(data, headersGetter) {
            var j = JSON.parse(data);
            var ret = j.objects;
            return ret;
          }]
      }
    });
  })

  /* Shopping cart */
  .factory('Cart', ['Product', function(Product) {
    var shoppingCart = {};
    var stats = {sum: 0, numItems: 0};

    return {
      addProduct: function(productId) {
        Product.get({'productId': productId}, function (p, getResponseHeaders) {
            stats.sum += parseFloat(p.gross_unit_price);
            stats.numItems ++;

            // Merge purchases of same product
            if (shoppingCart[productId] === undefined) {
              shoppingCart[productId] = { 'product': p, 'quantity': 0 };
            }

            shoppingCart[productId].quantity ++;
        });
      },

      stats: stats,

      shoppingCart: shoppingCart,

      clear: function() {
        stats.sum = 0.0;
        stats.numItems = 0;

        // We cannot simply realloc shoppingCart, since it is exported to view. Delete all keys. 
        for (var prop in shoppingCart) {
          delete shoppingCart[prop];
        }
      },

      /* Converts shopping cart to a sale transaction */
      generateSale: function() {
        var t = {};

        t.id = null;
        t.reversal = false;
        t.state = 0;
        t.timestamp = Date.now();

        t.total_items = 0;
        t.total_mva = 0.0;
        t.net_total_price = 0.0; 
        t.gross_total_price = 0.0; 

        t.items = [];

        for (var i in shoppingCart) {
          var item = {};

          item.product = shoppingCart[i].product.resource_uri;

          item.amount = shoppingCart[i].quantity;
          item.id = null;

          // Mva and total calculations
          var gross_unit_price = parseFloat(shoppingCart[i].product.gross_unit_price);
          var net_unit_price = (gross_unit_price / (1 + parseFloat(shoppingCart[i].product.mva_rate) / 100));

          item.net_unit_price = net_unit_price;

          // Update totals
          t.net_total_price += (net_unit_price * shoppingCart[i].quantity);
          t.gross_total_price += (gross_unit_price * shoppingCart[i].quantity);
          t.total_mva += (gross_unit_price - net_unit_price) * item.amount;
          t.total_items += shoppingCart[i].quantity;


          t.items.push(item);
        }

        console.log(JSON.stringify(t));

        return t;
      },

    };
  }]);
