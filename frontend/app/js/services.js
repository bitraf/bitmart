'use strict';

/* Services */


angular.module('bitmart.services', ['ngResource']).
  value('version', '0.2')

  .factory('Product', function($http, $resource, $log) {
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

    };
  }]);
