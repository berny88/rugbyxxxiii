# -*- coding: utf-8 -*-
from datetime import datetime
import logging
import os
import re
from flask import Blueprint, request, render_template, redirect, url_for
import sqlite3
from uuid import uuid4

logger = logging.getLogger(__name__)
tools_page = Blueprint('tools_page', __name__,
                        template_folder='templates')


class DbManager:

    def dict_factory(self, cursor, row):
        """
        use to convert sqllite row into dict
        """
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    """
    Load all match from json file
    """
    def __init__(self):
        #self.DATE_FORMAT = '%d/%m/%Y %H:%M:%S'
        self.DATE_FORMAT = '%Y/%m/%d %H:%M:%S'
        con = sqlite3.connect('bet.db')
        self.db = con
        self.db.row_factory = self.dict_factory
        logger.debug(u'getDb::row_factory={}'.format(self.db.row_factory))
        logger.debug(u'getDb::init::db={}'.format(self.db))

    def datetime_parser(self, dct):
        for k, v in dct.items():
            if isinstance(v, str) and re.search("\ UTC", v):
                #print(u"k={}/v={}".format(k,v))
                #try:
                dct[k] = datetime.strptime(v, self.DATE_FORMAT)
                #except:
                #print("exception={}".format(sys.exc_info()[0]))
    #                pass
        return dct

    def my_json_encoder(self, obj):
        """Default JSON serializer."""
        logger.info(obj)
        if isinstance(obj, datetime):
            return obj.strftime(self.DATE_FORMAT)
        return obj

    def getDb(self):
        """ get SQL DB 
        :return: connection to sqllite
        """
        if (self.db is None):
            con = sqlite3.connect('bet.db')
            self.db = con
            self.db.row_factory = self.dict_factory
            logger.info(u'getDb::db={}'.format(self.db))
            logger.info(u'getDb::row_factory={}'.format(self.db.row_factory))

        return self.db


    def setDb(self, the_db):
        """ set SQL DB access """
        self.db=the_db


class BetProjectClass:
    def __str__(self):
        return str(self.__dict__)


class ToolManager(DbManager):

    def create_table(self, conn, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except sqlite3.Error as e:
            print(e)
            
    def initAdmin(self, conn):
        """ initialize 2 first admins (theBerny, Stephou)
        :param conn: Connection object
        """
        try:
            c = conn.cursor()
            uuid = str(uuid4())
            c.execute("""insert into BETUSER 
                        (uuid, nickName, email,isAdmin, validated)
                        values
                        ('{}', 'theBerny','bernard.bougeon@gmail.com', 1, 1);""".format(uuid))
           
            conn.commit()
        except sqlite3.Error as e:
            print(e)

    def cleanUser(self):
        """
        delete all user in DB
        """
        conn = self.getDb()
        try:
            c = conn.cursor()
            uuid = str(uuid4())
            c.execute("""delete from betuser;""")
            conn.commit()
        except sqlite3.Error as e:
            print(e)

    def cleanBet(self):
        """
        delete all user in DB
        """
        conn = self.getDb()
        try:
            c = conn.cursor()
            uuid = str(uuid4())
            c.execute("""delete from bet;""")
            conn.commit()
        except sqlite3.Error as e:
            print(e)

    def initGames(self):
        """
        delete all user in DB
        """
        conn = self.getDb()
        try:
            c = conn.cursor()
            logger.info(u'initGames::delete from GAME')
            c.execute("""delete from GAME;""")
            uuid = str(uuid4())
            thestr = "INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool A','{}','2024/06/14 19:00:00','Germany','ALL','Scotland','SCO');".format(uuid)
            logger.info(u'initGames::{}'.format(thestr))
            c.execute(thestr)
            logger.info(u'initGames::after insert GAME')
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool A','{}','2024/06/15 13:00:00','Hungary','HON','Switzerland','SWI');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool B','{}','2024/06/15 16:00:00','Spain','ESP','Croatia','CRO');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool B','{}','2024/06/15 19:00:00','Italy','ITA','Albania','ALB');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool D','{}','2024/06/16 13:00:00','Poland','POL','Netherlands','HOL');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool C','{}','2024/06/16 16:00:00','Slovenia','SLO','Denmark','DAN');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool C','{}','2024/06/16 19:00:00','Serbia','SER','England','ENG');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool E','{}','2024/06/17 13:00:00','Romania','ROU','Ukraine','UKR');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool E','{}','2024/06/17 16:00:00','Belgium','BEL','Slovakia','SLO');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool D','{}','2024/06/17 19:00:00','Austria','AUT','France','FRA');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool F','{}','2024/06/18 16:00:00','Türkiye','TUR','Georgia','GEO');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool F','{}','2024/06/18 19:00:00','Portugal','POR','Czechia','CZE');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool B','{}','2024/06/19 13:00:00','Croatia','CRO','Albania','ALB');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool A','{}','2024/06/19 16:00:00','Germany','ALL','Hungary','HON');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool A','{}','2024/06/19 19:00:00','Scotland','ECO','Switzerland','SWI');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool C','{}','2024/06/20 13:00:00','Slovenia','SLO','Serbia','SER');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool C','{}','2024/06/20 16:00:00','Denmark','DAN','England','ENG');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool B','{}','2024/06/20 19:00:00','Spain','ESP','Italy','ITA');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool E','{}','2024/06/21 13:00:00','Slovakia','SLO','Ukraine','UKR');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool D','{}','2024/06/21 16:00:00','Poland','POL','Austria','AUT');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool D','{}','2024/06/21 19:00:00','Netherlands','HOL','France','FRA');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool F','{}','2024/06/22 13:00:00','Georgia','GEO','Czechia','CZE');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool F','{}','2024/06/22 16:00:00','Türkiye','TUR','Portugal','POR');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool E','{}','2024/06/22 19:00:00','Belgium','BEL','Romania','ROU');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool A','{}','2024/06/23 19:00:00','Switzerland','SWI','Germany','ALL');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool A','{}','2024/06/23 19:00:00','Scotland','ECO','Hungary','HON');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool B','{}','2024/06/24 19:00:00','Albania','ALB','Spain','ESP');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool B','{}','2024/06/24 19:00:00','Croatia','CRO','Italy','ITA');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool D','{}','2024/06/25 16:00:00','Netherlands','HOL','Austria','AUT');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool D','{}','2024/06/25 16:00:00','France','FRA','Poland','POL');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool C','{}','2024/06/25 19:00:00','England','ENG','Slovenia','SLO');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool C','{}','2024/06/25 19:00:00','Denmark','DAN','Serbia','SER');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool E','{}','2024/06/26 16:00:00','Slovakia','SLO','Romania','ROM');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool E','{}','2024/06/26 16:00:00','Ukraine','UKR','Belgium','BEL');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool F','{}','2024/06/26 19:00:00','Georgia','GEO','Portugal','POR');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Pool F','{}','2024/06/26 19:00:00','Czechia','CZE','Türkiye','TUR');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Finale phase','{}','2024/06/29 16:00:00','2A','','2B','');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Finale phase','{}','2024/06/29 19:00:00','1A','','2C','');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Finale phase','{}','2024/06/30 16:00:00','1C','','3D/E/F','');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Finale phase','{}','2024/06/30 19:00:00','1B','','3A/D/E/F','');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Finale phase','{}','2024/07/01 16:00:00','2D','','2E','');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Finale phase','{}','2024/07/01 19:00:00','1F','','3A/B/C','');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Finale phase','{}','2024/07/02 16:00:00','1E','','3A/B/C/D','');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Finale phase','{}','2024/07/02 19:00:00','1D','','2F','');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Finale phase','{}','2024/07/05 16:00:00','To be announced','','To be announced','');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Finale phase','{}','2024/07/05 19:00:00','To be announced','','To be announced','');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Finale phase','{}','2024/07/06 16:00:00','To be announced','','To be announced','');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Finale phase','{}','2024/07/06 19:00:00','To be announced','','To be announced','');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Finale phase','{}','2024/07/09 19:00:00','To be announced','','To be announced','');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Finale phase','{}','2024/07/10 19:00:00','To be announced','','To be announced','');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""INSERT INTO GAME (category, key, date, libteamA, teamA, libteamB, teamB) values ('Finale phase','{}','2024/07/14 19:00:00','To be announced','','To be announced','');""".format(uuid))            
            conn.commit()
        except sqlite3.Error as e:
            print(e)


    def createDb(self):
        conn = self.getDb()
        sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS BETUSER (
                                        uuid text PRIMARY KEY,
                                        nickName text NOT NULL,
                                        country text,
                                        description text,
                                        avatar text,
                                        hashedpwd text,
                                        email text,
                                        isAdmin INTEGER,
                                        validated INTEGER
                                    ); """
        self.create_table(conn, sql_create_projects_table)
        sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS GAME (
                                        key text PRIMARY KEY,
                                        date text ,
                                        teamA text,
                                        teamB text,
                                        libteamA text,
                                        libteamB text,
                                        resultA integer,
                                        resultB integer,
                                        category text,
                                        categoryName text
                                    ); """
        self.create_table(conn, sql_create_projects_table)
        sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS BET (
                                        uuid text PRIMARY KEY,
                                        FK_GAME text NOT NULL,
                                        FK_USER text NOT NULL,
                                        resultA integer,
                                        resultB integer,
                                        nbPoints integer
                                    ); """
        self.create_table(conn, sql_create_projects_table)
        sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS PROP (
                                        key text PRIMARY KEY,
                                        value text NOT NULL
                                    ); """
        self.create_table(conn, sql_create_projects_table)

        sql_all_tab="""SELECT name FROM sqlite_master WHERE type='table';"""
        cur = conn.cursor()
        cur.execute(sql_all_tab)

        rows = cur.fetchall()

        for row in rows:
            logger.info(row)

        #TODO : to remove param insert ?
        try:
            c = conn.cursor()
            uuid = str(uuid4())
            c.execute("""insert into PROP 
                        (key, value)
                        values
                        ('url_root', 'https://2023xvrugby.pythonanywhere.com/');""")
           
            conn.commit()
        except sqlite3.Error as e:
            print(e)
        


    def getProperties(self):
        """ get the complete list of properties"""
        localdb = self.getDb()
        sql_all_properties="""SELECT key, value FROM PROP;"""
        cur = localdb.cursor()
        cur.execute(sql_all_properties)

        rows = cur.fetchall()

        result = list()
        for row in rows:
            logger.info(u'\tprop={}'.format(row))
            result.append(row)
        return result

    def saveProperty(self, key, value):
        """ save a property"""
        localdb = self.getDb()

        #select prop by key - to insert or update
        try:
            c = localdb.cursor()
            p = self.getProperty(key)
            if p is None:
                logger.info(u'insert prop={}/{}'.format(key, value))
                c.execute("""insert into PROP 
                            (key, value)
                            values
                            ('{}', '{}');""".format(key, value))
            else:
                logger.info(u'update prop={}/{}'.format(key, value))
                c.execute("""update PROP 
                            set value='{}'
                            where key = '{}');""".format(value, key))
            localdb.commit()
        except sqlite3.Error as e:
            print(e)

        logger.info(u'saveProperty={}/{}'.format(key, value))

    def getProperty(self, key):
        """ get one property by key"""
        localdb = self.getDb()
        c = localdb.cursor()
        c.execute("select key, value from PROP where key='{}'".format(key))
        
        prop =  c.fetchone()
        if prop is None:
            prop=dict()
            prop[u"key"]=u""
            prop[u"value"]=u"http://localhost:5000"
        return prop



@tools_page.route('/properties/', methods=['GET'])
def properties():
    """
    """
    logger.info("properties::request:{} / {}".format(request.args, request.method))
    manager = ToolManager()
    propertyList = manager.getProperties()
    logger.info("properties::propertyList={}".format(propertyList ))
    #Add ever a new property to display a field
    prop = dict()
    prop[u"key"]=u""
    prop[u"value"]=u""
    propertyList.append(prop)

    return render_template('properties.html',
        propertyList=propertyList)

@tools_page.route('/saveproperties/', methods=['POST'])
def saveproperties():
    """
    """
    logger.info("saveproperties::request:{} / {}".format(request.args, request.method))
    logger.info("\tsaveproperties::request.values:{}".format(request.values))
    propDict=dict()
    for key, value in request.values.items():
        logger.info("saveproperties::key=[{}] / value=[{}]".format(key, value))
        if key != "submit" :
            #the value contains the key as prefix.
            # example : key001_key=key001 or key001_value=theValue
            # for new key :
            # example : new.key_key=ponpon or new.key_value=theNewValue
            # we analyze only key=xxx_value
            if (key.split("_")[1] == u"value"):
                #extract keyCode
                keyCode = key.split("_")[0]
                #case of new key/value
                if (u"_value" == key):
                    keyCode = request.values.get(u"_key")

                logger.info("\tsaveproperties::keyCode=[{}] ".format(keyCode))
                if (keyCode != u""):
                    if keyCode in propDict:
                        prop = propDict[keyCode]
                        prop[u"value"] = value
                        logger.info("\t\tsaveproperties::keyCode in propDict=[{}] ".format(prop))
                    else:
                        prop = dict()
                        prop[u"key"] = keyCode
                        prop[u"value"] = value
                        propDict[keyCode]=prop
                        logger.info("\t\tsaveproperties::keyCode not in propDict=[{}]".format(prop))
                    logger.info("\tsaveproperties::propDict=[{}] ".format(propDict))
            if (key.split("_")[1] == u"key"):
                value = request.values.get(key.split("_")[0] + "value")
                if (value ==""):
                    logger.info("\t\tsaveproperties::key=[{}] to remove".format(key))

    for keyProp in propDict:
        prop = propDict[keyProp]
        logger.info("saveproperties:: final list: prop=[{}]".format(prop))
        manager = ToolManager()
        manager.saveProperty(prop[u"key"], prop[u"value"])

    return redirect(url_for('tools_page.properties'))