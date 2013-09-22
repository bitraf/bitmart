'use strict';

/* Controllers */

angular.module('bitmart.controllers', ['ngRoute']).

  controller('ProductListCtrl', ['$scope', '$http', '$routeParams', 'Product', 'Cart',
             function($scope, $http, $routeParams, Product, Cart) {
    $scope.products = Product.query();

    $scope.categoryId = $routeParams.categoryId;

    // Get all categories
    $http.get('/api/category/?format=json').success(function(data) {
      $scope.categories = data.objects;
    });


    // Cart functionality
    $scope.cart = Cart;

  }])


  .controller('ProductDetailCtrl', ['$scope', '$routeParams', 'Product',
        function($scope, $routeParams, Product) {

    $scope.product = Product.get({productId: $routeParams.productId});
  }]);



function CategoriesCtrl($scope, $http) {

    $scope.categoryId = 1;
};
  
