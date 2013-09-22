'use strict';


// Declare app level module which depends on filters, and services
angular.module('bitmart', ['ngRoute', 'bitmart.filters', 'bitmart.services', 'bitmart.directives', 'bitmart.controllers']).
  config(function($routeProvider) {
    $routeProvider.when('/category/:categoryId', {templateUrl: 'partials/productList.html', controller: 'ProductListCtrl'});
    $routeProvider.when('/products/:productId', {templateUrl: 'partials/productDetail.html', controller: 'ProductDetailCtrl'});
    $routeProvider.when('/about', {templateUrl: 'partials/about.html'});
    $routeProvider.otherwise({redirectTo: '/category/1'});
  });
