betApp.directive('customPopover', function ($http,$timeout) {
    return {
        restrict: 'A',
        link: function (scope, el, attrs) {

            el.bind('click', function(e) {

                    $http.get('bets/apiv1.0/bets/'+attrs.popoverKey+'/rates')
                    .then(function(answer, status, headers, config) {

                        $(el).popover({
                            trigger: 'focus',
                            html:true,
                            title: 'Trends',
                            content: '<table><tr><td>Number of players</td><td>: '+answer.data.rates.nbBets +'</td></tr><tr><td>TeamA winner</td><td>: '+data.rates.winnerAPercent+'%</td></tr>'+'<tr><td>Draw</td><td>: '+data.rates.drawPercent+'%</td></tr>'+'<tr><td>TeamB winner</td><td>: '+data.rates.winnerBPercent+'%</td></tr></table>',
                            placement: attrs.popoverPlacement});
                        $(el).popover('show');

                    },
                    function(data, status, headers, config) {
                        if (status==-1) {
                            //do nothing
                        }else {
                            showAlertError("Erreur lors de la récupération des statistiques ; erreur HTTP : " + status);
                        }
                    });
            })
        }
    };
});

betApp.controller('BetsCtrl', ['$scope', '$routeParams', '$http', '$q', '$location', '$timeout', '$window',
                            function ($scope, $routeParams, $http, $q, $location, $timeout, $window) {

        var canceler = $q.defer();

        $('#pleaseWaitDialog').modal('hide');

        // to split the table of bets :
        $scope.onlyGroupeFilter = function (bet) {
            return bet.category === 'GROUPE';
        };
        $scope.onlyFinalFilter = function (bet) {
            return bet.category === 'FINAL';
        };

        
        
        $scope.getBetsByCommunityId = function() {
            
            $scope.bets = {};
            $scope.displaySaveButton = false;

            hideAlerts();

            $('#spin_bets_groupe').show();
            $('#spin_bets_final').show();
            console.log("getBetsByCommunityId");

            if (isConnected($window)) {
                //$http.get('communities/apiv1.0/communities/'+ com_id + '/users/'+ getConnectedUser($window).user_id +'/bets ', {timeout: canceler.promise})
                $http.get('bets/apiv1.0/'+ getConnectedUser($window).user_id +'/bets', {timeout: canceler.promise})
                .then(function(answer, status, headers, config) {
                    $scope.bets = answer.data;
                    console.log("getBetsByCommunityId::bets=", $scope.bets);

                    // to disable the input fields in the form
                    $scope.displaySaveButton = true;
                    $scope.bets.bets.forEach(function(bet) {
                        bet.notClosed=!bet.blocked;
                    });


                    
                },
                function(data, status, headers, config) {
                    if (status==-1) {
                        //do nothing
                    }else {
                        showAlertError("Erreur lors de la récupération de la liste des paris ; erreur HTTP : " + status);
                    }
                    $('#spin_bets_groupe').hide();
                    $('#spin_bets_final').hide();
                    
                });
            }

        }

 
        $scope.saveBets = function() {

            $('#pleaseWaitDialog').modal('show');

            $http.put('bets/apiv1.0/'+ getConnectedUser($window).user_id +'/bets', {bets: $scope.bets.bets, timeout: canceler.promise})
            .then(function(answer, status, headers, config) {
                //showAlertSuccess("Paris sauvegardés !");
                $.notify("Bets saved !" , "success");
                $('#pleaseWaitDialog').modal('hide');
            },
            function(data, status, headers, config) {
                if (status==-1) {
                    //do nothing
                } else if (status==403){
                    showAlertError("Même pas en rêve ! status=" + status+ " " + data);
                } else {
                    showAlertError("Erreur lors de la création des paris ; erreur HTTP : " + status);
                }
                $('#pleaseWaitDialog').modal('hide');
            })
        }

        // Aborts the $http request if it isn't finished.
        $scope.$on('$destroy', function(){
            hideAlerts();
            canceler.resolve();
        });

}]);