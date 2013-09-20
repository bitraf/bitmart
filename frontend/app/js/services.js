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
//            ret.meta = j.meta;
            return ret;
          }]
      }
  });
});

//isArray:true,
