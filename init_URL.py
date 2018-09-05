# -*- coding: utf-8 -*-
import datetime
import concurrent.futures
import requests
import collections
import threading
import ReadGoogle
import urllib.request as req
import mysql.connector
from mysql.connector import Error
import configparser

HEADERS = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    #'Host': None,
    'If-Modified-Since': '0',
    #'Referer': None,
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
}

def init_requests():
    session = requests.Session()
    session.headers.update(HEADERS)
    return session

def write_db(url,response,dt,version,conn):
    query = "INSERT INTO api_snapshot (url,response,create_time,version) " \
            "VALUES(%s,%s,%s,%s)"
    args = (url,response,dt,version)
    try:
        
 
        cursor = conn.cursor()
        cursor.execute(query, args)
 
        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')
 
        conn.commit()
    except Error as error:
        print(error)
def init_database(session,urls,dbconn):
    for url in urls:
        raw_response=session.get(url[0])
        if len(url)>1 and len(url[1])>0:
            response = raw_response.content[raw_response.find(url[1])+len(url[1]):]
        else:
            response=raw_response.content

        
        #ok binance but not huobi, #response = req.urlopen(url)
        print(response)
        if raw_response.status_code == 200:
                write_db(url[0],response,datetime.datetime.now(),0,dbconn)


    pass

# Retrieve a single page and report the URL and contents
def load_url(session, url):
    response = session.get(url)
    if response.get_code() == 200:
        # You can refactor this part and
        # make it run in another thread
        # devoted to handling local IO tasks,
        # to reduce the burden of Net IO worker threads
        return handle_response(response,url)
def db_connect(config):
    #https://stackoverflow.com/questions/42906665/import-my-database-connection-with-python
    

    try:
        
        dbconn = mysql.connector.connect(host = config['mysqlDB']['host'],
                           database = config['mysqlDB']['database'],user = config['mysqlDB']['user'],
                           password = config['mysqlDB']['password']
                           )

       
        if dbconn.is_connected():
            print('Connected to MySQL database')
            return dbconn
    
    
    except Exception as err:
        print (err)
    

config = configparser.ConfigParser()
config.read('dbconfig.ini')
dbconn=db_connect(config)
URLS = ReadGoogle.ReadGoogle(config['G']['sheetid'],0,1,'exchange')
init_database(init_requests(),URLS,dbconn)
