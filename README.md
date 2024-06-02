# Generic simple bet web site
small web bet site in python

## From Pythoneverywhere

To initialize git env

* cd mysite

* git init

* git remote add origin https://github.com/yourusername/yourreponame.git

* git pull https://github.com/yourusername/yourreponame.git master


then

git fetch bet

git pull

Forcer theBerny isAdmin : no secu
users/apiv1.0/admin/forceTheBerny

## run from your PC
go to your source directory (cd xxxxx)

set FLASK_APP=flask_app

flask run

## Initialization of the DB

1. call http://URL/users/apiv1.0/admin/initDB (will just create empty tables if not created)

1. register your email (you can see your uuid when, after conection, you click on your name in right top of the banner)

1. call http://URL/users/apiv1.0/admin/forceTheBerny/<your uuid> (to force your account as admin) : only 1 Admin can be created

1. call http://URL/users/apiv1.0/admin/initGames to initialize the games of tournament (today hard coded in the sources)

