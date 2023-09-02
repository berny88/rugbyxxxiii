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
            c.execute("""delete from GAME;""")
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool A', 'Pool A-FRA-NZL', '2023/09/08 19:15:00', 'France', 'FRA', 'New Zealand', 'NZL');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool A', 'Pool A-ITA-NAM', '2023/09/09 11:00:00', 'Italy', 'ITA', 'Namibia', 'NAM');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool B', 'Pool B-IRL-ROM', '2023/09/09 13:30:00', 'Ireland', 'IRL', 'Romania', 'ROU');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool C', 'Pool C-AUS-GEO', '2023/09/09 16:00:00', 'Australia', 'AUS', 'Georgia', 'GEO');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool D', 'Pool D-ENG-ARG', '2023/09/09 19:00:00', 'England', 'ENG', 'Argentina', 'ARG');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool D', 'Pool D-JAP-CL', '2023/09/10 11:00:00', 'Japan', 'JAP', 'Chile', 'CHL');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool B', 'Pool B-ZAF-SCO', '2023/09/10 15:45:00', 'South Africa', 'AFG', 'Scotland', 'SCO');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool C', 'Pool C-WAL-FID', '2023/09/10 19:00:00', 'Wales', 'WAL', 'Fiji', 'FID');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool A', 'Pool A-FRA-URU', '2023/09/14 19:00:00', 'France', 'FRA', 'Uruguay', 'URU');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool A', 'Pool A-NZL-NAM', '2023/09/15 19:00:00', 'New Zealand', 'NZL', 'Namibia', 'NAM');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool D', 'Pool D-SAM-CL', '2023/09/16 13:00:00', 'Samoa', 'SAM', 'Chile', 'CHL');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool C', 'Pool C-WAL-POR', '2023/09/16 15:45:00', 'Wales', 'WAL', 'Portugal', 'POR');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool B', 'Pool B-IRL-TON', '2023/09/16 19:00:00', 'Ireland', 'IRL', 'Tonga', 'TON');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool B', 'Pool B-ZAF-ROM', '2023/09/17 13:00:00', 'South Africa', 'AFG', 'Romania', 'ROU');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool C', 'Pool C-AUS-FID', '2023/09/17 15:45:00', 'Australia', 'AUS', 'Fiji', 'FID');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool D', 'Pool D-ENG-JAP', '2023/09/17 19:00:00', 'England', 'ENG', 'Japan', 'JAP');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool A', 'Pool A-ITA-URU', '2023/09/20 15:45:00', 'Italy', 'ITA', 'Uruguay', 'URU');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool A', 'Pool A-FRA-NAM', '2023/09/21 19:00:00', 'France', 'FRA', 'Namibia', 'NAM');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool D', 'Pool D-ARG-SAM', '2023/09/22 15:45:00', 'Argentina', 'ARG', 'Samoa', 'SAM');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool C', 'Pool C-GEO-POR', '2023/09/23 12:00:00', 'Georgia', 'GEO', 'Portugal', 'POR');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool D', 'Pool D-ENG-CL', '2023/09/23 15:45:00', 'England', 'ENG', 'Chile', 'CHL');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool B', 'Pool B-ZAF-IRL', '2023/09/23 19:00:00', 'South Africa', 'AFG', 'Ireland', 'IRL');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool B', 'Pool B-SCO-TON', '2023/09/24 15:45:00', 'Scotland', 'SCO', 'Tonga', 'TON');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool C', 'Pool C-WAL-AUS', '2023/09/24 19:00:00', 'Wales', 'WAL', 'Australia', 'AUS');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool A', 'Pool A-URU-NAM', '2023/09/27 15:45:00', 'Uruguay', 'URU', 'Namibia', 'NAM');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool D', 'Pool D-JAP-SAM', '2023/09/28 19:00:00', 'Japan', 'JAP', 'Samoa', 'SAM');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool A', 'Pool A-NZL-ITA', '2023/09/29 19:00:00', 'New Zealand', 'NZL', 'Italy', 'ITA');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool D', 'Pool D-ARG-CL', '2023/09/30 13:00:00', 'Argentina', 'ARG', 'Chile', 'CHL');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool C', 'Pool C-FID-GEO', '2023/09/30 15:45:00', 'Fiji', 'FID', 'Georgia', 'GEO');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool B', 'Pool B-SCO-ROM', '2023/09/30 19:00:00', 'Scotland', 'SCO', 'Romania', 'ROU');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool C', 'Pool C-AUS-POR', '2023/10/01 15:45:00', 'Australia', 'AUS', 'Portugal', 'POR');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool B', 'Pool B-ZAF-TON', '2023/10/01 19:00:00', 'South Africa', 'AFG', 'Tonga', 'TON');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool A', 'Pool A-NZL-URU', '2023/10/05 19:00:00', 'New Zealand', 'NZL', 'Uruguay', 'URU');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool A', 'Pool A-FRA-ITA', '2023/10/06 19:00:00', 'France', 'FRA', 'Italy', 'ITA');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool C', 'Pool C-WAL-GEO', '2023/10/07 13:00:00', 'Wales', 'WAL', 'Georgia', 'GEO');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool D', 'Pool D-ENG-SAM', '2023/10/07 15:45:00', 'England', 'ENG', 'Samoa', 'SAM');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool B', 'Pool B-IRL-SCO', '2023/10/07 19:00:00', 'Ireland', 'IRL', 'Scotland', 'SCO');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool D', 'Pool D-JAP-ARG', '2023/10/08 11:00:00', 'Japan', 'JAP', 'Argentina', 'ARG');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool B', 'Pool B-TON-ROM', '2023/10/08 15:45:00', 'Tonga', 'TON', 'Romania', 'ROU');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Pool C', 'Pool C-FID-POR', '2023/10/08 19:00:00', 'Fiji', 'FID', 'Portugal', 'POR');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Q1', 'Q1-Winner Pool C-Runner-up Pool D', '2023/10/14 15:00:00', 'W_PC', 'Winner Pool C', 'R_PD', 'Runner-up Pool D');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Q2', 'Q2-Winner Pool B-Runner-up Pool A', '2023/10/14 19:00:00', 'W_PB', 'Winner Pool B', 'R_PA', 'Runner-up Pool A');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Q3', 'Q3-Winner Pool D-Runner-up Pool C', '2023/10/15 15:00:00', 'W_PD', 'Winner Pool D', 'R_PC', 'Runner-up Pool C');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('Q4', 'Q4-Winner Pool A-Runner-up Pool B', '2023/10/15 19:00:00', 'W_PA', 'Winner Pool A', 'R_PB', 'Runner-up Pool B');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('S1', 'S1-W_Q1-W_Q2', '2023/10/20 19:00:00', 'W_Q1', 'W_Q1', 'W_Q2', 'W_Q2');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('S2', 'S2-W_Q3-W_Q4', '2023/10/21 19:00:00', 'W_Q3', 'W_Q3', 'W_Q4', 'W_Q4');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('F1', 'F1-L_S1-L_S2', '2023/10/27 19:00:00', 'L_S1', 'L_S1', 'L_S2', 'L_S2');""".format(uuid))
            uuid = str(uuid4())
            c.execute("""insert into GAME (category, key, date, libteamA, teamA, libteamB, teamB) values('F2', 'F2-W_L1-W_L1', '2023/10/28 19:00:00', 'W_L1', 'W_L1', 'W_L1', 'W_L1');""".format(uuid))
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
        self.initAdmin(conn)



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