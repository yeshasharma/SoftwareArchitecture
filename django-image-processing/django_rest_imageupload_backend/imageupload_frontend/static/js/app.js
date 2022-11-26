var myApp = angular.module('imageuploadFrontendApp', ['ngResource']);

myApp.config(function($resourceProvider) {
    $resourceProvider.defaults.stripTrailingSlashes = false;
});

myApp.config(['$qProvider', function ($qProvider) {
    $qProvider.errorOnUnhandledRejections(false);
}]);

myApp.controller('MainCtrl', function($scope, Images, $http)
{
    console.log('In main control');
    $scope.images = Images.query();
    $scope.newImage = {};

    $scope.uploadImage = function(images, checkedOptions)
    {
        console.log('Upload Image called');
        // $scope.newImage.image = $scope.newImage.image[0];

      console.log(images);
      //console.log(checkedOptions);
     // console.log(images[0].image);
      $http({method:'POST', url: '/operations/', data:{'pk': images[0].pk, 'image': images[0].image, 'checkedOptions': checkedOptions}})
        .then(function successCallback(response)
        {
            console.log('success');
        });
    };
});

myApp.directive('filesModel', filesModelDirective);