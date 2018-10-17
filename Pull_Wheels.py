from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from urllib.request import urlretrieve

import re

from selenium.webdriver.support.ui import WebDriverWait

def find(driver):
    element = driver.find_elements_by_xpath("//a[contains(@href,'.whl')]")
    if element:
        return element
    else:
        return False


'''azure-mgmt-datalake-store==0.5.0
azure-mgmt-nspkg==2.0.0
azure-mgmt-resource==2.0.0
azure-nspkg==2.0.0
protobuf==3.5.1
google-cloud-bigquery==1.1.0
google-cloud-core==0.28.1
fastavro==0.17.5
'''
str="""
oauthlib==2.0.6
onedrivesdk==1.1.8"""


res=re.findall("(.*)(?:==)",str)

driver = webdriver.Firefox()



for r in res:
    driver.get('https://pypi.org/project/'+r+'/#files')
    #print("goes: "+'https://pypi.org/project/'+r+'/#files')
    search3 = driver.find_elements_by_xpath("//a[contains(@href,'.whl')]")
    #search3 = WebDriverWait(driver, 8).until(find)
    sleep(5)
    for down in search3:
        addr=down.get_attribute("href")
        print("downloading:  "+down.text+"  from "+addr)
        
        
        urlretrieve(addr, down.text)
        sleep(2)
    sleep(5)
'''
import urllib2

url = "http://download.thinkbroadband.com/10MB.zip"

file_name = url.split('/')[-1]
u = urllib2.urlopen(url)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])
print "Downloading: %s Bytes: %s" % (file_name, file_size)

file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print status,

f.close()
'''
