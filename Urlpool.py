# -*- coding: utf-8 -*-

import concurrent.futures
import requests
import collections
import threading
import ReadGoogle
import urllib.request as req
import mysql.connector
from mysql.connector import Error
import configparser

# URL Pool  URLS = ["http://google.com","http://baidu.com"

# Time interval (in seconds)
INTERVAL = 5 * 60

# The number of worker threads
MAX_WORKERS = 2

# You should set up request headers
# if you want to better evade anti-spider programs
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

############################
def db_connect(config):
    #https://stackoverflow.com/questions/42906665/import-my-database-connection-with-python
    

    try:
        
        dbconn = mysql.connector.connect(host = config['mysqlDB']['host'],
                           database = config['mysqlDB']['database'],user = config['mysqlDB']['user'],
                           password = config['mysqlDB']['password']
                           )

       
        
    
    except Exception as err:
        print (err)
    if dbconn.is_connected():
            print('Connected to MySQL database')
            return dbconn
    

def get_info_db(sql,addr,version=0,date='1990-01-01'):
    # version=0 means latest
    
    if date>'1990-01-01':
        sql=sql+"select balance, create_time from balance_history where address='"+add+"'"
        sql=sql+" and date>"
    sql=sql+" order by CreateTime desc"
    try:
        dbconn = mysql.connector.connect(host='localhost',database='python_mysql',user='root',password='secret')
        if conn.is_connected():
            print('Connected to MySQL database')
            cursor = dbconn.cursor()
            cursor.execute(sql)
            results = cursor.fetchall
            for row in results:
                print (row[0])
            if count(queryresult)>=version:

                    queryresult[version]
    except Exception as err:
        print (err)


    pass
    return balance
def alarm(msg):
    pass

def handle_response(response,url):
    # TODO implement your logics here !!!
    query="select content, createtime from APISnapshot where url='"+url+"' order by createtime desc"
    cursor = db_connect().cursor()
    cursor.execute(sql)
    result = cursor.fetchone
    if result != response:
                "insert into APISnapshot values('"+url+"','"+response+"',"+datenow()+")"
                alarm(response - result)


    get_infodb_()
    print ("response")

# Retrieve a single page and report the URL and contents
def load_url(session, url):
    response = session.get(url)
    if response.status_code == 200:
        # You can refactor this part and
        # make it run in another thread
        # devoted to handling local IO tasks,
        # to reduce the burden of Net IO worker threads
        return handle_response(response,url)

# Generate a session object
def init_requests():
    session = requests.Session()
    session.headers.update(HEADERS)
    return session

config = configparser.ConfigParser()
config.read('dbconfig.ini')
db_connect(config)
URLS = ReadGoogle.ReadGoogle(config['G']['sheetid'],'exchange')

# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor, init_requests() as session:
    deque = collections.deque(URLS)
    rlock = threading.RLock()
    cond = threading.Condition(rlock)

    print ("start with")

    def wind_up(url):
        with cond:
            deque.append(url)
            cond.notify()

    while True:
        url = None

        # Retrieve task content
        with cond:
            while not len(deque) > 0:
                cond.wait()
            url = deque.popleft()
            print (url)

        # Work
        executor.submit(load_url, session, url)

        threading.Timer(INTERVAL, wind_up, url)