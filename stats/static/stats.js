betApp.controller('statsRankingCtrl', ['$scope', '$routeParams', '$http', '$q', '$location', '$timeout', '$window',
    function ($scope, $routeParams, $http, $q, $location, $timeout, $window) {
        var canceler = $q.defer();

        // to avoid the cache of the images (avatars)
        d = new Date();
        $scope.currentDateForAvoidTheCache = d.getTime();
    
        $scope.getRanking = function(category) {
            $('#spin').show();
            $('#spinRanking').show();
            $('#divRanking').hide();
    
            if (category == 'Pool') {
                $('#btn-groupe').addClass('active');
                $('#btn-final').removeClass('active');
                $('#btn-all').removeClass('active');
            } else if (category == 'Q') {
                $('#btn-groupe').removeClass('active');
                $('#btn-final').addClass('active');
                $('#btn-all').removeClass('active');
            } else {
                $('#btn-groupe').removeClass('active');
                $('#btn-final').removeClass('active');
                $('#btn-all').addClass('active');
            }
            console.log("ranking category=", category);
            $http.get('/stats/apiv1.0/stats/ranking?filter='+category, {timeout: canceler.promise})
            .then(function(answer) {
                $scope.rankings = answer.data;
                console.log("ranking answer.data=", answer.data);
                $('#spin').hide();
                $('#spinRanking').hide();
                $('#divRanking').show();
            },
            function(data, status, headers, config) {
                if (status==-1) {
                    //do nothing
                } else {
                    showAlertError("Erreur lors de la récupération du classement général ; erreur HTTP : " + status);
                }
                $('#spin').hide();
                $('#spinRanking').hide();
            });
        }
    
    
    
        // Aborts the $http request if it isn't finished.
        $scope.$on('$destroy', function(){
            hideAlerts();
            canceler.resolve();
        });
                                
}]);
