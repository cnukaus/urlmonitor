# urlmonitor
detecting changes of a webpage and store to database

run Urlpool_master.py

Just need to config your own dbconfig.ini file for connectivity

Should be html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
otherwise driver.page_source maybe un rendered HTML/script
