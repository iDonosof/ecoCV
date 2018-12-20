'use strict';

/**
 * @ngdoc function
 * @name ecocvApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the ecocvApp
 */
angular.module('ecocvApp')
  .controller('MainCtrl', ['$scope', function ($scope) {
    $scope.qrString = '';
    $scope.qrToGenerate = '';
  }]);
