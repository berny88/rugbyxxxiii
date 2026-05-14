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

        $scope.getBetsUsers = function() {
            
            $scope.bets = {};
            $scope.displaySaveButton = false;

            hideAlerts();

            $('#spin_bets_groupe').show();
            $('#spin_bets_final').show();
            console.log("getBetsUsers");

            if (isConnected($window)) {
                $http.get('bets/apiv1.0/bets_users', {timeout: canceler.promise})
                .then(function(answer, status, headers, config) {
                    $scope.betsUsers = answer.data.betsUsers;
                    console.log("getBetsUsers::betsUsers=", $scope.betsUsers);
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
        
        /**
         * Affiche une modal de confirmation Bootstrap
         * et appelle ask_ai1() si l'utilisateur confirme
         */
        $scope.askAIWithConfirmation = function(agent_name){
            console.log('Ask ' + agent_name + ' - Showing confirmation modal');
            $('#confirmAsk'+agent_name+'Modal').modal('show');
        }

        /**
         * Confirme l'action et génère les valeurs aléatoires
         */
        $scope.confirmAsk = function(agent_name){
            $('#confirmAsk'+agent_name+'Modal').modal('hide');
            $scope.ask_ai1();
        }

        /**
         * Annule l'action
         */
        $scope.cancelAsk = function(agent_name){
            $('#confirmAsk'+agent_name+'Modal').modal('hide');
            console.log('Ask ' + agent_name + ' - Action cancelled');
        }

        /**
         * Vérifie si un élément est visible à l'écran
         * Retourne true si l'élément n'est pas caché par ng-show ou display:none
         */
        var isElementVisible = function(element) {
            // offsetParent est null si l'élément ou un de ses parents est caché (display: none)
            if (element.offsetParent === null) {
                return false;
            }
            // Vérification supplémentaire du style display
            var style = window.getComputedStyle(element);
            return style.display !== 'none' && style.visibility !== 'hidden';
        };

        /**
         * Génère des valeurs aléatoires pour tous les champs de paris
         * Remplit les champs resultA et resultB avec des nombres entre 0 et 5
         * Ignore les champs masqués (ng-show ou display: none)
         */
        $scope.ask_ai1 = function(){
            // Sélectionne tous les champs input de type number
            var inputs = document.querySelectorAll('input[type="number"]');
            inputs.forEach(function(input) {
                // Vérifie que l'input n'est pas désactivé et qu'il est visible
                console.log('Ask AI - Processing input:', input.name, 'disabled:', input.disabled, 'visible:', isElementVisible(input));
                if (!input.disabled && isElementVisible(input)) {
                    // Génère un nombre aléatoire entre 0 et 5
                    var randomValue = Math.floor(Math.random() * 6);
                    input.value = randomValue;
                    
                    // Déclenche l'événement input pour que Angular détecte la modification
                    var event = new Event('input', { bubbles: true });
                    input.dispatchEvent(event);
                }
            });
            
            console.log('Ask AI - Random values generated for all visible bet fields');
        }
}]);