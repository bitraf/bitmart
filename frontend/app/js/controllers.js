'use strict';

/* Controllers */

angular.module('bitmart.controllers', []).

  controller('ProductListCtrl', function($scope, Product) {
    $scope.products = Product.query();

//$http.get('/api/product/?format=json').success(function(data) {
//      $scope.products = data.objects;
//    })
  })

  .controller('ProductDetailCtrl', ['$scope', '$routeParams', 'Product',
        function($scope, $routeParams, Product) {

    $scope.product = Product.get({productId: $routeParams.productId});
  }]);
