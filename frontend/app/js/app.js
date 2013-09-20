'use strict';


// Declare app level module which depends on filters, and services
angular.module('bitmart', ['ngRoute', 'bitmart.filters', 'bitmart.services', 'bitmart.directives', 'bitmart.controllers']).
  config(function($routeProvider) {
    $routeProvider.when('/products', {templateUrl: 'partials/productList.html', controller: 'ProductListCtrl'});
    $routeProvider.when('/products/:productId', {templateUrl: 'partials/productDetail.html', controller: 'ProductDetailCtrl'});
    $routeProvider.otherwise({redirectTo: '/products'});
  });
