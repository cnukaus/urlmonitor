# urlmonitor
## also can use GoogleSheets function to parse page directly such as ethereum address

Google Sheets直接解析：
=CONCATENATE("https://etherscan.io/address/",B2,"#code")
=IMPORTxml(E2,"//div/span[@class='h6 font-weight-bold mb-0'")


detecting changes of a webpage and store to database

run Urlpool_master.py

Just need to config your own dbconfig.ini file for connectivity

Should be html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
otherwise driver.page_source maybe un rendered HTML/script
