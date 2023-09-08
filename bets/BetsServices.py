# -*- coding: utf-8 -*-
import logging

from datetime import datetime, timedelta
from flask import Blueprint, jsonify, request, session
from uuid import uuid4
import sqlite3
from games.GameServices import GamesManager
from bets.BetsTools import BetsManager
from bets.BetsTools import Bet

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

