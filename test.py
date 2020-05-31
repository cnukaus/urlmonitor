# -*- coding: utf-8 -*-

import concurrent.futures
import requests
import queue
import threading
import datetime
import ReadGoogle
import urllib.request as req
import mysql.connector
import configparser
import json_parse
from mysql.connector import Error
from warnings import warn

warnings.warn(DeprecationWarning("test.py has been deprecated"), stacklevel=2)

# Time interval (in seconds)
INTERVAL = 0.25 * 60

# The number of worker threads
MAX_WORKERS = 4

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
    # see https://stackoverflow.com/questions/42906665/import-my-database-connection-with-python
    try:
        dbconn = mysql.connector.connect(host = config['mysqlDB']['host'],
                                             database = config['mysqlDB']['database'],user = config['mysqlDB']['user'],
                                             password = config['mysqlDB']['password']
                                        )
    except Exception as err:
        print("exception"+err)
    if dbconn.is_connected():
        print('Connected to MySQL database')
        return dbconn

def handle_response(response,url,dbconn):
    print("handle")
    query = "SELECT response, create_time FROM api_snapshot WHERE url='"+url+"' AND version=0 ORDER BY create_time DESC"
    cursor = dbconn.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    if result is not None:
        # print('%s' %response,create_date )# %(response,create_time))
        print("old value"+result[0][:20])
        print(response[:20])
        if result[0] != response:
                    write_db(url,response,datetime.datetime.now(),0,dbconn)
                    alarm(response, result)


        #get_info_db(query,url,dbconn,0,datetime.datetime.now())
        
    else:
        print("first write"+response[:20])
        write_db(url,response,datetime.datetime.now(),0,dbconn)

def get_info_db(sql,addr,dbconn,version=0,date='1990-01-01'):
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
            results = cursor.fetchall()
            for row in results:
                print (row[0])
            if count(queryresult)>=version:

                    queryresult[version]
    except Exception as err:
        print ("exception2"+err)


    pass
    return balance
def alarm(msg,msg2=None, extra=None):
    print(f"alarm with msg{'2' if extra else ''} str():")
    print(msg)
    print("and repr():")
    print(repr(msg))
    if msg2 is not None:
        alarm(msg2, extra=True)
    print("" if extra else "alarm() done")

def write_db(url,response,dt,version,conn):
    query0 = "UPDATE api_snapshot set version=NULL where url=%s"
    args0 =(url,)
    query = ("INSERT INTO api_snapshot (url,response,create_time,version) "
            "VALUES(%s,%s,%s,%s)")
    args = (url, response, dt, version)
    try:
        print(query0 + str(url))
        cursor = conn.cursor(buffered=True) #bug as init_URL didn't require buffered
        cursor.execute(query0, args0)
        print("overwrite verion")
        cursor.execute(query, args)
        conn.commit()
        print("writedb")
        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')
        conn.commit()
    except Error as error:
        print("write Db err:"+str(error))
# Retrieve a single page and report the URL and contents
def load_url(session, url,dbconn):
    print("load_url1")
    raw_response = session.get(url) #init_requests()#
    print (url+"http code %d" %(raw_response.status_code))#"parsedJson:"+json)
    json=json_parse.parsejson(raw_response.content.decode("utf-8"),url) #decode from binary b'string'
    print (json)
    if raw_response.status_code == 200:
        # You can refactor this part and
        # make it run in another thread
        # devoted to handling local IO tasks,
        # to reduce the burden of Net IO worker threads
        return handle_response(json,url,dbconn)
def ThreadPoolExecutor():
    return concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS)

# Generate a session object
def Session():
    session = requests.Session()
    session.headers.update(HEADERS)
    return session

def _main():
    config = configparser.ConfigParser()
    config.read('dbconfig.ini')
    dbconn=db_connect(config)
    #load_url(Session(),'https://api.coinex.com/v1/market/list',dbconn)
    return load_url(Session(),'https://api.kucoin.com/v1/market/open/symbols',dbconn)

if __name__ == "__main__":
    url = _main()
    print("DONE")

# TODO: remove once not necessary or obsolete

#$REMOVED$:URLS = ReadGoogle.ReadGoogle(config['G']['sheetid'],0,1,'exchange')
#$REMOVED$:
#$REMOVED$:print (URLS)
#$REMOVED$:
#$COMMENT$:We can use a with statement to ensure threads are cleaned up promptly
#$REMOVED$:with ThreadPoolExecutor() as executor, Session() as session:
#$REMOVED$:    if not URLS:
#$REMOVED$:        raise RuntimeError('Please fill in the array `URLS` to start probing!')
#$REMOVED$:
#$REMOVED$:    tasks = queue.Queue()
#$REMOVED$:
#$REMOVED$:    for urlArray in URLS:
#$REMOVED$:        url=urlArray[0]
#$REMOVED$:        print(url)
#$REMOVED$:        tasks.put_nowait(url)
#$REMOVED$:
#$REMOVED$:    def wind_up(url):
#$REMOVED$:        #print('wind_up(url={})'.format(url))
#$REMOVED$:        tasks.put(url)
#$REMOVED$:
#$REMOVED$:    while True:
#$REMOVED$:        url = tasks.get()
#$COMMENT$:        Work
#$REMOVED$:        executor.submit(load_url, session, url,dbconn)
#$REMOVED$:        threading.Timer(interval=INTERVAL, function=wind_up, args=(url,)).start()
