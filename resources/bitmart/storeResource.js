'use strict';

angular.module('storeResource', [ 'ngResource' ]).factory('Faktura', function ($resource) {
  return $resource(fiken.url.fakturaDataFakturanummer(':fakturanummer'), {fakturanummer: '@fakturanummer'}, {
sendEpostmelding: { method: 'POST', params: {cmd: "sendEpostmelding", tilEpost:'@tilEpost', tilNavn: '@tilNavn'} }
,opprettHandelsutkast: { method: 'POST', params: {cmd: "opprettHandelsutkast"} }
,opprettKomplettKreditnota: { method: 'POST', params: {cmd: "opprettKomplettKreditnota"} }
});
    });

