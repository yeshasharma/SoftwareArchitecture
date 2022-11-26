"use strict";
function transformImageRequest(data) {
    if (data === undefined)
        return data;

    var fd = new FormData();
    angular.forEach(data, function(value, key) {
      if (value instanceof FileList) {
        if (value.length == 1) {
          fd.append(key, value[0]);
        } else {
          angular.forEach(value, function(file, index) {
            fd.append(key + '_' + index, file);
          });
        }
      } else {
        fd.append(key, value);
      }
    });

    return fd;
}

myApp.factory('Images', function($resource) {
    return $resource("/api/images/:pk/", {'pk': '@pk'}, {
        'save': {
            'method': 'POST',
            'transformRequest': transformImageRequest,
            'headers': {'Content-Type': undefined}
            }
    });
});