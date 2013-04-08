var clerk = angular.module('clerk', []).config(function ($routeProvider) {
  $routeProvider.
    when('/', {controller: StoreCtrl, templateUrl: "/resources/bitmart/clerk/clerk.html"});
});
