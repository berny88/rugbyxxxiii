# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request, session
import logging
import math
import sqlite3
from tools.Tools import DbManager, ToolManager
from users.UserServices import UserManager
from bets.BetsTools import BetsManager
from bets.BetsTools import Bet

logger = logging.getLogger(__name__)

games_page = Blueprint('games_page', __name__,
                       template_folder='templates', static_folder='static')



@games_page.route('/games', methods=['GET'])
def gameslist():
    return games_page.send_static_file('games.html')


@games_page.route('/apiv1.0/gameslist', methods=['GET'])
def getGames():
    mgr = GamesManager()
    games=mgr.getAllGames()
    logger.info(">>{}".format(jsonify({'games': games}).data))

    return jsonify({'games': games})

@games_page.route('/apiv1.0/games', methods=['PUT'])
def updateGamesResults():
    u"""
    save the result of games.
    only allowed to admin
    :return the numbers of games updated
    """
    logger.info("updateGamesResults::{}".format(request.json["games"]))
    if "no_save" in request.json:
        no_save=request.json["no_save"]
    else:
        no_save=False
    logger.info("updateGamesResults::no_save={}".format(no_save))
    if "cookieUserKey" in session:
        mgr = GamesManager()
        gamesjson = request.json["games"]
        cookieUserKey = session['cookieUserKey']
        user_mgr = UserManager()
        user = user_mgr.getUserByUserId(cookieUserKey)
        logger.info(u"updateGamesResults::cookieUserKey by ={}".format(cookieUserKey))
        logger.info(u"updateGamesResults::update by ={}".format(user.email))
        nbHit=0
        if user.isAdmin:
            nbHit = mgr.update_all_games(gamesjson, no_save)
        else:
            logger.info(u"updateGamesResults::No Admin = 403")
            return "Ha ha ha ! Mais t'es pas la bonne personne pour faire ça, mon loulou", 403
        return jsonify({'nbHit': nbHit})
    else:
        return "Ha ha ha ! Mais t'es qui pour faire ça, mon loulou ?", 403


u"""
**************************************************
Service layer
"""


class Match:
    u""""
     "key": "GROUPEE_SWE_BEL",
       "teamA": "SWE",
       "teamB": "BEL",
       "libteamA": "SUEDE",
       "libteamB": "BELGIQUE",
       "dateMatch": "22/06/2016 21:00:00",
       "dateDeadLineBet": "",
       "resultA": "",
       "resultB": "",
       "category": "GROUPE",
       "categoryName": "GROUPEE"
    """""
    def __init__(self):
        self.key = u""
        self.teamA = u""
        self.teamB = u""
        self.libteamA = u""
        self.libteamB = u""
        self.resultA=-1
        self.resultB=-1
        self.category = u""
        self.categoryName = u""


    def convertFromBson(self, elt):
        u"""
        convert a community object from mongo
        :param elt: bson data from mongodb
        :return: nothing
        """
        for k in elt.keys():
            if k == "_id":
                self._id = str(elt[k])
            else:
                self.__dict__[k] = elt[k]


    def convertIntoBson(self):
        u"""
        convert a community object into mongo Bson format
        :return: a dict to store in mongo as json
        """
        elt = dict()
        for k in self.__dict__:
            if k == "_id" and self._id is not None:
                elt[k] = ObjectId(self._id)
            else:
                elt[k] = self.__dict__[k]
        return elt


    def computeResult(self, bet):
        u"""
            Si le parieur a trouvé le vainqueur (ou deviné un match nul) : 5 points
            3 points si le parieur a deviné le nombre de point d'une équipe
            2 points si le parieur a deviné la bonne différence de points entre les 2 équipes (peu importe le vainqueur)
            Donc, pour chaque match, un parieur peut récolter 5 + 6 + 2 points = 13 points s'il devine le résultat exact du match
        """
        nb_point=0

        #tool = ToolManager()
        #str_nb=tool.getProperty(key="NB_POINT_TEAM")["value"]
        #if str_nb=="":
        NB_POINT_TEAM=3
        #else:
    #    NB_POINT_TEAM=int(str_nb)

    #str_nb=tool.getProperty(key="NB_POINT_WINNER")["value"]
        #    if str_nb=="":
        NB_POINT_WINNER=5
        #else:
    #    NB_POINT_WINNER=int(str_nb)

    #str_nb=tool.getProperty(key="NB_POINT_DIFF")["value"]
        #   if str_nb=="":
        NB_POINT_DIFF=2
        #else:
    #    NB_POINT_DIFF=int(str_nb)

        #change nbpoints only if rightmatch
        logger.info(u'\Game::computeResult=game key={}/bet key={}'.format(self.key, bet.game_id))
        if (self.key==bet.game_id):
            if (bet.resultA!="") and (bet.resultB!="") and (self.resultA!="") and (self.resultB!="") and  (bet.resultA is not None) and (bet.resultB is not None) and (self.resultA is not None) and (self.resultB is not None):
                logger.info(u'\t\tMatchs::computeResult=bet.resA={} - self.resA={}'.format(bet.resultA,self.resultA))
                logger.info(u'\t\tMatchs::computeResult=bet.resA={} - self.resA={}'.format(bet.resultB,self.resultB))
                #3 points si le parieur a deviné le nombre de point d'une équipe
                if bet.resultA==self.resultA:
                    nb_point=nb_point+NB_POINT_TEAM
                if bet.resultB == self.resultB:
                    nb_point = nb_point + NB_POINT_TEAM
                # 2 points si le parieur a deviné la bonne différence de points entre les 2 équipes (peu importe le vainqueur)
                if math.fabs(self.resultA-self.resultB) == math.fabs(bet.resultA-bet.resultB):
                    nb_point = nb_point + NB_POINT_DIFF
                #5 pts if 1N2
                if  (((self.resultA-self.resultB) >0 and (bet.resultA-bet.resultB)>0) or
                    ((self.resultA - self.resultB) < 0 and (bet.resultA - bet.resultB) < 0) or
                    ((self.resultA - self.resultB) == 0 and (bet.resultA - bet.resultB) == 0)):
                    nb_point = nb_point+NB_POINT_WINNER
                #logger.info(u'\t\tMatchs::computeResult=nb_point={}'.format(nb_point))
        #finally we update nb of points
        bet.nbPoints = nb_point
        logger.info(u'\t\tMatchs::computeResult=nb_point={}'.format(bet.nbPoints))

class GamesManager(DbManager):

    def getAllMatchs(self):
        return self.getAllGames()

    def getAllGames(self):
        """
        get the complete list of matchs
        """
        """
        get the complete list of matchs
        """
        localdb = self.getDb()

        """uuid, nickName, desc, avatar, email, isAdmin"""

        sql_all_games="""SELECT category, key, date, libteamA, teamA, libteamB, teamB,
            resultA, resultB
                        FROM GAME order by date, key;"""
        cur = localdb.cursor()
        cur.execute(sql_all_games)

        rows = cur.fetchall()
        result = list()
        for row in rows:
            result.append(row)                    
            logger.info("game={}".format(row))
        return result


    def update_all_games(self, games_to_update, no_save):
        #load all match from db (because we just want to update result
        logger.info(u"update_all_games::start-games to update {}".format(games_to_update))
        nb_hits=0
        bet_mgr = BetsManager()
        for gameFromClient in games_to_update:
            game = Match()
            game.convertFromBson(gameFromClient)
            game_key=game.key
            logger.info(u'\tupdate_all_games::try update game : >>{}'.format(game_key))
            betList = bet_mgr.getBetsOfGame(game_key)
            # mettre à jour juste les resultats
            logger.info(u'\tupdate_all_games::try update game :{}'.format(game))
            try:
                localdb = self.getDb()
                c = localdb.cursor()
                c.execute("""update GAME 
                            set resultA=?, resultB=?
                            where
                            key=?""", (game.resultA, game.resultB, game.key))  
                localdb.commit()
                        
            except sqlite3.Error as e:
                logger.error(e)
                logger.info(u'\tid : {}'.format(gameFromClient))
                localdb.rollback()
                logger.info(u'update_all_matchs::rollback')
            nb_hits = nb_hits + 1
            # pour chaque match demander à betmanager de calculer le nb de points de chq bet
            # le principe sera de calculer le nbde pts d'un user = somme de ses paris
            for bet in betList:
                game.computeResult(bet)
                logger.info(
                    u'\t\tupdate_all_matchs::bet={}/{} - nbpts={}'.format(bet.game_id, bet.user_id, bet.nbPoints))
                bet_mgr.saveScore(bet)
         


        return None


    def format_bet(self, bet, game):
        result = u"<tr>"
        result = result + u"<td>" + game.key+"</td><td>"+game.teamA+"</td><td>"+game.teamB+"</td>"
        result = result + u"<td>" + str(game.resultA)+"</td><td>"+str(game.resultB)+"</td><td>&nbsp;&nbsp;</td>"
        result = result + u"<td>" + bet.key+"</td><td>"+bet.com_id+"</td><td>"+bet.user_id+"</td>"
        result = result + u"<td>" + str(bet.resultA)+"</td><td>"+ str(bet.resultB)+"</td><td>"+str(bet.nbpoints) + u"<td>"
        result = result + u"</tr>"
        return result






