betApp.controller('gamesCtrl', ['$scope', '$http', '$q', '$timeout', '$window', function ($scope, $http, $q, $timeout, $window) {

        var canceler = $q.defer();

        $scope.getGames = function() {
            $http.get('games/apiv1.0/gameslist', {timeout: canceler.promise})
            .then(function(answer) {
                //ng-repeat :
                $scope.games = answer.data.games;
                $scope.displaySaveButton = false;
                if (isConnected($window)) {
                    $scope.displaySaveButton = true;
                }
            });
            $scope.displayBlogPostSaveButton = false;
            console.log("getGames::isConnected($window)="+isConnected($window));
            if (isAdmin($window)) {
                $scope.displayBlogPostSaveButton =true;
            }
        }

        $scope.getGamesOfTheDay = function() {
            $http.get('games/apiv1.0/games', {timeout: canceler.promise})
            .then(function(answer) {

                $scope.allGames = answer.data.games;
                $scope.games = [];
                var now = new Date();
                $scope.displayGamesOfTheDay = false;

                $scope.allGames.forEach(function(game) {
                        var gameDate = new Date(game.dateMatch);
                        //var matchDate = Date.parse(match.dateMatch)
                        //var timeDiff = Math.abs(matchDate - now.getTime());
                        //if (Math.ceil(timeDiff / (1000 * 3600 * 24)) == 1) {
                        if (((gameDate.getDate() - now.getDate()) == 0)
                            && ((gameDate.getMonth() - now.getMonth()) == 0)
                            && ((gameDate.getYear() - now.getYear()) == 0)) {
                            $scope.games.push(game)
                            $scope.displayGamesOfTheDay = true;
                        }
                })
            });
        }

        $scope.saveGames = function() {
            $('#pleaseWaitDialog').modal('show');
            console.log("saveGames::$scope.no_save="+$scope.no_save);
            $http.put('games/apiv1.0/games', {games: $scope.games, no_save: $scope.no_save, timeout: canceler.promise})
            .then(function(data, status, headers, config) {
                //showAlertSuccess("Paris sauvegardés !");
                $('#pleaseWaitDialog').modal('hide');
                $.notify("games saved !" , "success");
            },
            function(data, status, headers, config) {
                $('#pleaseWaitDialog').modal('hide');
                if (status==-1) {
                    //do nothing
                } else if (status==403){
                    showAlertError("Même pas en rêve ! status=" + status+ " " + data);
                } else {
                    showAlertError("Erreur lors de la mise à jour des games ; erreur HTTP : " + status);
                }
            })
        }

        $scope.createHistoryRankings = function() {
            $('#spin_histo').show();
            $('#pleaseWaitDialog').modal('show');
            $http.put('stats/apiv1.0/stats/historyrankings', {timeout: canceler.promise})
            .then(function(data, status, headers, config) {
                $('#pleaseWaitDialog').modal('hide');
                $.notify("Historique des classements enregistrés !" , "success");
                $('#spin_histo').hide();
            },
            function(data, status, headers, config) {
                $('#pleaseWaitDialog').modal('hide');
                if (status==-1) {
                    //do nothing
                } else if (status==403){
                    showAlertError("Même pas en rêve ! status=" + status+ " " + data);
                } else {
                    showAlertError("Erreur lors de l'enregistrement de l'historique des classements ; erreur HTTP : " + status);
                }
                $('#spin_histo').hide();
            })
        }

        // to avoid the cache of the images (avatars)
        d = new Date();
        $scope.currentDateForAvoidTheCache = d.getTime();

        $scope.getEmails = function() {
            $http.get('/users/apiv1.0/users_for_admin?validated=true', {timeout: canceler.promise})
            .then(function(answer) {
                $scope.users = answer.data.users;

                tabEmails = [];
                for (var index = 0; index < $scope.users.length; ++index) {
                    user = $scope.users[index];
                    console.log("user=", user)
                    tabEmails.push(user.email);
                }
                $scope.listEmails = tabEmails.join(" ; ");
            });
        }

        $scope.$on('$destroy', function(){
            canceler.resolve();  // Aborts the $http request if it isn't finished.
        });


}]);