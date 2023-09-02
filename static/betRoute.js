// configure our routes
betApp.config(function($routeProvider) {


    $routeProvider

        // route for index
        .when('/home', { templateUrl:'static/home.html', controller:'indexCtrl' })
        .when('/accueil2', { templateUrl:'static/accueil.html', controller:'UsersListCtrl' })
        .when('/accueil3', { templateUrl:'static/accueil.html', controller:'UsersListCtrl' })
        .when('/', { templateUrl:'static/home.html', controller:'UsersListCtrl' })

        //subscription process
        // to subscribe to the site
        .when('/signon', { templateUrl:'users/static/logon.html', controller:'indexCtrl' })
        // just page to confirm email sent
        .when('/logon_successfull', { templateUrl:'users/static/logon_successfull.html', controller:'indexCtrl' })

        // route for list of users
        .when('/users', { templateUrl:'users/static/users.html', controller:'UsersListCtrl' })
        // user page modification
        .when('/user_detail/:user_id', { templateUrl:'users/static/user.html', controller:'UserDetailCtrl' })

        // to sign in
        .when('/signin', { templateUrl:'users/static/signin.html', controller:'LoginCtrl' })
        // to logout
        .when('/logout', { templateUrl:'users/static/logout.html', controller:'LogoutCtrl' })

		.when('/bets', { templateUrl:'bets/static/bets.html', controller:'BetsCtrl' })

        // route for matchs page: "static page"
        .when('/matchs', { templateUrl:'matchs/static/calendrier.html', controller:'matchsCtrl' })
        .when('/admin_matchs', { templateUrl:'matchs/static/admin_matchs.html', controller:'matchsCtrl' })

        // route for stats: "buble graph" & ranking
        .when('/stats_ranking', { templateUrl:'stats/static/stats_ranking.html', controller:'statsRankingCtrl' })
        .when('/stats_global', { templateUrl:'stats/static/stats_global.html', controller:'statsRankingCtrl' })
        .when('/stats_historyranking', { templateUrl:'stats/static/stats_historyranking.html', controller:'statsRankingCtrl' })

        // route for tirage: "static page"
        .when('/tirage', { templateUrl:'static/tirage.html', controller:'tirageCtrl' })

        // route for calendrier: "static page"
        .when('/calendrier', { templateUrl:'static/calendrier.html', controller:'calendrierCtrl' })

        // route for pictures and videos
        .when('/entertainment', { templateUrl:'static/entertainment.html', controller:'indexCtrl' })

        // route for rules of games and bets : "static page"
        .when('/rules', { templateUrl:'static/rules.html', controller:'indexCtrl' })

        // route for about page : "static page"
        .when('/about', { templateUrl:'static/about.html', controller:'indexCtrl' })

        // route for about page : "static page"
        .when('/contact', { templateUrl:'static/contact.html', controller:'indexCtrl' })

        // default
        .otherwise({ templateUrl:'static/home.html', controller:'indexCtrl' });
});