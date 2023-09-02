// create the module and name it betApp
// also include ngRoute for all our routing needs
var betApp = angular.module('betApp', ['ngRoute', 'ngResource', 'ngAnimate', 'ngSanitize']);

// To avoid HTML caching :
betApp.run(function($rootScope, $templateCache) {
    $rootScope.$on('$routeChangeStart', function(event, next, current) {
        if (typeof(current) !== 'undefined'){
            $templateCache.remove(current.templateUrl);
        }
    });
});

// create the controller and inject Angular's $scope
betApp.controller('indexCtrl', function($scope, $window) {
    $scope.message = 'RUGBY 2023';
    $scope.comment = 'Amazing bet site';
    $scope.isConn = false;
    //console.log("indexCtrl::load::$scope.isConn=", $scope.isConn);
    //alert("indexCtrl::load::isConn="+$scope.isConn);
        
    $scope.indexIsConnected = function() {
        $scope.isConn = isConnected($window);
        //alert("indexCtrl::isConn="+$scope.isConn);
        console.log("indexCtrl::$scope.isConn=", $scope.isConn);
        return $scope.isConn;
    }

    function js_yyyy_mm_dd_hh_mm_ss (myDate) {
      year = "" + myDate.getFullYear();
      month = "" + (myDate.getMonth() + 1); if (month.length == 1) { month = "0" + month; }
      day = "" + myDate.getDate(); if (day.length == 1) { day = "0" + day; }
      hour = "" + myDate.getHours(); if (hour.length == 1) { hour = "0" + hour; }
      minute = "" + myDate.getMinutes(); if (minute.length == 1) { minute = "0" + minute; }
      second = "" + myDate.getSeconds(); if (second.length == 1) { second = "0" + second; }
      return year + "-" + month + "-" + day + " " + hour + ":" + minute + ":" + second;
    }

    $scope.injectCounter = function() {

        var startDateUTC = new Date('9/20/2019 15:00:00 UTC');
        $scope.startDateLocal = js_yyyy_mm_dd_hh_mm_ss(startDateUTC);

        // injection in HTML :
        $("#counter").html("<div id='DateCountdown' data-date='"+$scope.startDateLocal+"' style='width: 100%;'></div>");

        $("#DateCountdown").TimeCircles({
            "animation": "smooth",
            "bg_width": 1.2,
            "fg_width": 0.1,
            "circle_bg_color": "#60686F",
            "time": {
                "Days": {
                    "text": "Days",
                    "color": "#FFCC66",
                    "show": true
                },
                "Hours": {
                    "text": "Hours",
                    "color": "#99CCFF",
                    "show": true
                },
                "Minutes": {
                    "text": "Minutes",
                    "color": "#BBFFBB",
                    "show": true
                },
                "Seconds": {
                    "text": "Seconds",
                    "color": "#FF9999",
                    "show": true
                }
            }
        });
    }

});

// create the controller and inject Angular's $scope
betApp.controller('topbarCtrl', function($scope, $window, $rootScope) {
    // security.js
    if (isConnected($window)) {
        $("#connectedUserInTopbar").html(getConnectedUser($window).nickName);
        $rootScope.user_id = getConnectedUser($window).user_id;
    }

    // to display the button "connexion" or "deconnexion" in the topbar
    $scope.isConnected = function() {
        // security.js :
        return isConnected($window);
    }
});

// create the controller and inject Angular's $scope
betApp.controller('calendrierCtrl', function($scope, $window) {

});

// create the controller and inject Angular's $scope
betApp.controller('tirageCtrl', function($scope, $window) {

});

//Go to top
jQuery(document).ready(function() {
    var offset = 200;
    var duration = 500;
    jQuery(window).scroll(function() {
        if (jQuery(this).scrollTop() > offset) {
            jQuery('.scroll-to-top').fadeIn(duration);
        } else {
            jQuery('.scroll-to-top').fadeOut(duration);
        }
    });

    jQuery('.scroll-to-top').click(function(event) {
        event.preventDefault();
        jQuery('html, body').animate({scrollTop: 0}, duration);
        return false;
    })
});
