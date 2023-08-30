# -*- coding: utf-8 -*-
import logging

from datetime import datetime, timedelta
from flask import Blueprint, jsonify, request, session
from uuid import uuid4
import sqlite3
from games.GameServices import GamesManager

from tools.Tools import DbManager, BetProjectClass
from users.UserServices import UserManager

logger = logging.getLogger(__name__)

bets_page = Blueprint('bets_page', __name__,
                      template_folder='templates', static_folder='static')


@bets_page.route('/betslist', methods=['GET'])
def bets():
    return bets_page.send_static_file('bets.html')


@bets_page.route('/apiv1.0/<user_id>/bets', methods=['GET'])
def getBets(user_id):
    u"""
    return the list of all bets of a user in a community.
    If user has never bet, we return the list of Matchs.
    :param user_id: id of user (uuid)
    :return:  a json form for the list of bet
    """
    mgr = GamesManager()
    game_list = mgr.getAllMatchs()
            
    betsMgr = BetsManager()
    bets = betsMgr.getBetsOfUser(user_id, game_list)

    logger.debug(u" ------------ ")
    logger.info(u"getBets::bets={}".format(bets))
    return jsonify({'bets': bets})

@bets_page.route('/apiv1.0/<user_id>/bets', methods=['PUT'])
def createOrUpdateBets( user_id):
    u"""
    save the list of bets of a user in a community.
    the list of bets is defined inrequest.json.
    :param user_id: id of user (uuid)
    :return the numbers of bets created or updated
    """
    betslist = request.json["bets"]
    logger.info(u"saveBets::bets={} ".format(betslist))

    if "cookieUserKey" in session:
        cookieUserKey = session['cookieUserKey']
        logger.info(u"saveBets::cookieUserKey={} ".format(cookieUserKey))
        if (cookieUserKey == user_id):
            betsMgr = BetsManager()
            bets = betsMgr.createOrUpdateBets(user_id, betslist)
            #this.games
            logger.debug(u" ------------ ")
            logger.debug(u"getBets::bets={}".format(bets))
            return jsonify({'data': "great, U R the best !"})
            return jsonify({'nbHit': nbHit})
        else:
            return "Ha ha ha ! Mais t'es pas la bonne personne pour faire ça, mon loulou", 403


@bets_page.route('/apiv1.0/bets/<key>/rates', methods=['GET'])
def getRatesOfAMatch(key):
    mgr = BetsManager()
    rates=mgr.getRatesOfAMatch(key)
    logger.info(">>{}".format(jsonify({'rates': rates}).data))
    return jsonify({'rates': rates})

class Bet(BetProjectClass):
    u""""
    _id (soit uuid soit objectid mongo)
    user_id (=uuid)
    key : "GROUPEE_SWE_BEL"
    category (GROUPE, 1_4, 1_2, 1_1, 1)
    categoryName (groupeA, Quart 01, Demi 02...)
    dateDeadLineBet :  date limite de saisi du pari
    dateMatch : date match pour info
    libteamA: nom equipe A
    libteamB: nom équipe B
    teamA : code Equipe A
    teamB : code Equipe A
    resultA : pari resutat teamA
    resultB : pari resutat teamB
    nbpoints : score calculated after the end of the match
    """""

    def __init__(self):
        self._id = None
        self.user_id = u""
        self.key = u""
        self.resultA = None
        self.resultB = None
        self.category = u""
        self.categoryName = u""
        self.libteamA = u""
        self.libteamB = u""
        self.teamA = u""
        self.teamB = u""
        self.nbpoints = 0

    def convertFromBson(self, elt):
        """
        convert a community object from mongo
        :param elt bson structure from mongodb
        """
        for k in elt.keys():
            if k == "_id":
                self._id = str(elt[k])
            else:
                self.__dict__[k] = elt[k]

    def convertIntoBson(self):
        """
        convert a community object into mongo Bson format
        """
        elt = dict()
        for k in self.__dict__:
            if k == "_id":
                logger.info(u'convertIntoBson={} - do nothing'.format(self._id))
                #if not self._id is None:
                #    logger.info(u'convertIntoBson={}'.format(self._id))
                #    elt[k] = ObjectId(self._id)
            else:
                elt[k] = self.__dict__[k]
        return elt


class BetsManager(DbManager):
    def getBetsOfUser(self, user_id, game_list):
        logger.info("getBetsOfUser::START **")
        localdb = self.getDb()
        result = list()
        # get all bets+games+user attrb
        sql_bets_by_user="""
            SELECT category, key, date, libteamA, teamA, libteamB, teamB,
            u.uuid, b.resultA, b.resultB, nbPoints, b.uuid as bet_uuid
            FROM GAME g, BETUSER u, BET b
            where  b.FK_GAME=g.key
            and b.FK_USER=u.uuid
            and u.uuid= :user_id
            order by g.date;"""
        cur = localdb.cursor()
        cur.execute(sql_bets_by_user, {'user_id':user_id})
        rows = cur.fetchall()
        logger.info("getBetsOfUser::rowcount=".format( cur.rowcount ))
        if len(rows) == 0:
            ##insert empty games by 1 sql and sequence or one by one with uuid ?
            logger.info("getBetsOfUser::no bet yet - need to initialized")
            #then reload
            for m in game_list:
                logger.info("getBetsOfUser::insert a new empty bet for {}/{}".format(m,user_id))
                uuid = str(uuid4())
                logger.info("getBetsOfUser::key={}".format(m['key']))
                cur.execute("""insert into BET 
                    (uuid, FK_GAME, FK_USER,nbPoints, resultA, resultB )
                    values
                    (?, ?, ?, 0, 0, 0);""", (uuid, m['key'], user_id))            
            localdb.commit()
            cur.execute(sql_bets_by_user, {'user_id':user_id})
            rows = cur.fetchall()
            logger.info("getBetsOfUser::reload bet::{}".format(len(rows)))
        for row in rows:
            bet = Bet()
            bet.bet_uuid=row["bet_uuid"]
            bet.user_id=row["uuid"]
            bet.game_id=row["key"]
            bet.dateMatch=row["date"]
            bet.category=row["category"]
            #2021/06/11 21:00:00
            bet.dateGameInDate=datetime.strptime(row["date"], self.DATE_FORMAT)
            currDate = datetime.now()
            dateToCompare = bet.dateGameInDate - timedelta(hours=2)
            if (dateToCompare<currDate):
                bet.blocked=True
            else:
                bet.blocked=False
            bet.resultA=row["resultA"]
            bet.resultB=row["resultB"]
            bet.libteamA = row["libteamA"]
            bet.libteamB = row["libteamB"]
            bet.teamA = row["teamA"]
            bet.teamB = row["teamB"]
            bet.nbPoints = row["nbPoints"]

            logger.info("getBetsOfUserAndCom::bet={}".format(row))
            tmpdict = bet.__dict__
            result.append(tmpdict)

        result.sort(key=lambda bet: bet["dateMatch"])

        return result

    def getBetsOfGame(self, game_key):
        logger.info("getBetsOfGame::START")
        localdb = self.getDb()
        result = list()
        # get all bets+games+user attrb
        sql_bets_by_user="""
            SELECT category, key, date, libteamA, teamA, libteamB, teamB,
            u.uuid, b.resultA, b.resultB, nbPoints, b.uuid as bet_uuid
            FROM GAME g, BETUSER u, BET b
            where  b.FK_GAME=g.key
            and b.FK_USER=u.uuid
            and b.FK_GAME= :fk_game
            order by g.date;"""
        cur = localdb.cursor()
        cur.execute(sql_bets_by_user, {'fk_game':game_key})
        rows = cur.fetchall()
        logger.info("getBetsOfGame::rowcount=".format( len(rows) ))

        for row in rows:
            bet = Bet()
            bet.bet_uuid=row["bet_uuid"]
            bet.user_id=row["uuid"]
            bet.game_id=row["key"]
            bet.dateMatch=row["date"]
            #2021/06/11 21:00:00
            bet.dateGameInDate=datetime.strptime(row["date"], self.DATE_FORMAT)
            bet.resultA=row["resultA"]
            bet.resultB=row["resultB"]
            bet.libteamA = row["libteamA"]
            bet.libteamB = row["libteamB"]
            bet.teamA = row["teamA"]
            bet.teamB = row["teamB"]
            bet.nbPoints = row["nbPoints"]

            logger.info("getBetsOfGame::bet={}".format(row))
            result.append(bet)

        
        return result

    def createOrUpdateBets(self, user_id, bets):
        u"""
        update a list af bet for user in a community
        :param user_id: id of user (to check with the detail of bet)
        :param bets: list of bets
        :return: nb of bets updated or created
        """
        nbHit = 0
        for b in bets:
            currDate = datetime.now()
            dateToCompare = datetime.strptime(b["dateMatch"], self.DATE_FORMAT) - timedelta(hours=2)
            logger.warn(u'\tcreateOrUpdateBets::try save : b={}\n'.format(b))
            logger.info(u'\t\t****** CtrlDateFront - currDate : {}/{}'.format(currDate, dateToCompare))
            if dateToCompare>currDate :
                if b["user_id"]==user_id :
                    self.createOrUpdate(b)
                    nbHit = nbHit + 1
                else:
                    logger.warn(u'\tcreateOrUpdateBets::pas le bon user: {}\n'.format(b))
            else:
                logger.warn(u'\tcreateOrUpdateBets::date limite dépassée, on n\'enregistre pas : {}\n'.format(b))
        return nbHit
    
    def createOrUpdate(self, bet):
        u"""
        store a bet (create is not exist or update)
        :param bet: the bet to create or update
        :return: the bet (i'm sure if it is good idea)
        """
        #update to do
        localdb = self.getDb()
        try:
            c = localdb.cursor()
            c.execute("""update BET 
                        set resultA='{}', resultB='{}'
                        where
                        uuid='{}'""".format(bet["resultA"], bet["resultB"], bet["bet_uuid"]))  
            localdb.commit()
                      
        except sqlite3.Error as e:
            logger.error(e)
            logger.info(u'\tid : {}'.format(bet))
            localdb.rollback()
            logger.info(u'createOrUpdate::rollback')
            return False

        return True

    def saveScore(self, bet):
        """
        store just nb points.
        :param bet: the bet to create or update
        :return: the bet (i'm sure if it is good idea)
        """
        logger.info(u'saveScore:: {}'.format(bet))
        betuui = bet.bet_uuid
        if betuui is None:
            logger.info(u"\t\tERROR - bet not found")
        else:
            try:
                localdb=self.getDb()
                c = localdb.cursor()
                c.execute("""update BET 
                            set nbPoints=?
                            where
                            uuid=?""", (bet.nbPoints, bet.bet_uuid))  
                localdb.commit()
                        
            except sqlite3.Error as e:
                logger.error(e)
                logger.info(u'\tid : {}'.format(bet))
                localdb.rollback()
                logger.info(u'createOrUpdate::rollback')
                return None
        return bet
    def saveScore(self, bet):
        u"""
        store just nb points.
        :param bet: the bet to create or update
        :return: the bet (i'm sure if it is good idea)
        """
        logger.info(u'saveScore:: {}'.format(bet))
        betuui = bet.bet_uuid
        if betuui is None:
            logger.info(u"\t\tERROR - bet not found")
        else:
            try:
                localdb=self.getDb()
                c = localdb.cursor()
                c.execute("""update BET 
                            set nbPoints=?
                            where
                            uuid=?""", (bet.nbPoints, bet.bet_uuid))  
                localdb.commit()
                        
            except sqlite3.Error as e:
                logger.error(e)
                logger.info(u'\tid : {}'.format(bet))
                localdb.rollback()
                logger.info(u'createOrUpdate::rollback')
                return None
        return bet

#   def delete(self, bet):
#        u"""
#        delete a bet
#        :param bet: bet to remove
#        :return: the nb of deletion
#        """
#        bsonBet = self.getDb().bets.find_one({"user_id": bet.user_id, "com_id": bet.com_id,
#                                              "key": bet.key})
#        result = self.getDb().bets.delete_one({"_id": bsonBet["_id"]})
#        return result.deleted_count


    def get_all_bets(self):
        betBsonList = self.getDb().bets.find()
        betList=list()
        for b in betBsonList:
            bet = Bet()
            bet.convertFromBson(b)
            betList.append(bet)
        return betList



    def getRatesOfAMatch(self,key):
        u"""
        rates of the players for a match
        :param key: the key of a bet (like GROUPEE_ITA_IRL)
        :return: the rates
        """
        bets = self.getDb().bets.find({"key":key})
        winnerA = 0
        winnerB = 0
        draw = 0
        nbBets = 0
        for bet in bets:
            if bet["resultA"] is not None and bet["resultB"] is not None:
                if bet["resultA"] == bet["resultB"]:
                    draw = draw + 1
                if bet["resultA"] > bet["resultB"]:
                    winnerA = winnerA + 1
                if bet["resultA"] < bet["resultB"]:
                    winnerB = winnerB + 1
                nbBets = nbBets + 1
        result = dict()
        result["key"] = key
        result["nbBets"] = nbBets
        result["winnerAPercent"] = int(winnerA * 100 / nbBets)
        result["drawPercent"] = int(draw * 100 / nbBets)
        result["winnerBPercent"] = 100 - result["winnerAPercent"] - result["drawPercent"]

        return result



