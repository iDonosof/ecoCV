'use strict';

/**
 * @ngdoc overview
 * @name ecocvApp
 * @description
 * # ecocvApp
 *
 * Main module of the application.
 */
angular
  .module('ecocvApp', ['ui.router'])
  .config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider){
    $urlRouterProvider.otherwise('/');
    $stateProvider.state('home', {
      url:'/',
      templateUrl:'views/main.html',
      controller: 'MainCtrl'
    });
  }]);
