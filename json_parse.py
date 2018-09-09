# -*- coding: utf-8 -*-
import json
from pprint import pprint
import ast

def parsejson(content,url):


	if "binance".upper() in  url.upper() and "allBookTickers".upper() in  url.upper():
	#binance

		data=json.loads(content) #load is URL, loads is string
		#for item in data:
		#		pprint(item["symbol"])
		return str([item["symbol"] for item in data])#data
	if "binance".upper() in  url.upper() and "exchangeInfo".upper() in  url.upper():
	#binance

		data=json.loads(str(content)[str(content).find("exchangeFilters\":[],\"symbols\":")+len("exchangeFilters\":[],\"symbols\":"):-1]) #load is URL, loads is string
		#for item in data:
		#		pprint(item["symbol"])
		return str([item["symbol"] for item in data])#data
	#bilaxy
	if "bilaxy".upper() in  url.upper():
# evalute a dict stored as string 
		value2 = ast.literal_eval(content)#'{"code":"200","data":[{"symbol":16,"high":"0.021"}]}') a dictionary with 2 pairs, pair 2 is another list of json dicts

		#for item in value2['data']:
		#	pprint(item["symbol"])
		return str([item["symbol"] for item in value2['data']])#value2['data']

	if "huobi".upper() in  url.upper():

		value2 = ast.literal_eval(content)#'{"code":"200","data":[{"symbol":16,"high":"0.021"}]}') a dictionary with 2 pairs, pair 2 is another list of json dicts

		#for item in value2['data']:
		#	pprint(item)
		return str(value2['data'])
	#bithumb, dictionary with 2 pairs, pair 2 is  a sub dict (last child pair is time and better to be removed?)
	if "bithumb".upper() in  url.upper():

		value2 = ast.literal_eval(content)
		
		#for item in value2['data'].keys():
		#	print(item)
		return str(sorted(list(value2['data'].keys())))

	#https://api.kucoin.com/v1/market/open/symbols
	## 这里可以先使用type(result_mid)看一下它是不是一个unicode，如果是的话再用encode转成你想要的编码
	if "kucoin".upper() in  url.upper() and "symbols".upper() in  url.upper() :

		value2 = json.loads(content)#'{"code":"200","data":[{"symbol":16,"high":"0.021"}]}') a dictionary with 2 pairs, pair 2 is another list of json dicts

		#for item in value2['data']:
		#	pprint(item["symbol"])
		return str([item["symbol"] for item in value2['data']])
	if "kucoin".upper() in  url.upper() and "/coins".upper() in  url.upper() :

		value2 = json.loads(content) #'{"success":true,"code":"OK","msg":"Operation succeeded.","timestamp":1536326724718,"data":[{"withdrawMinFee":0.5,"coinType":"ERC20","withdrawMinAmount":10.0,"withdrawRemark":"","orgAddress":null,"txUrl":"https://etherscan.io/tx/","userAddressName":null,"withdrawFeeRate":0.001,"confirmationCount":12,"infoUrl":null,"enable":true,"name":"Kucoin Shares","tradePrecision":4,"depositRemark":null,"enableWithdraw":true,"enableDeposit":true,"coin":"KCS"},{"withdrawMinFee":100.0,"coinType":"ERC20","withdrawMinAmount":500.0,"withdrawRemark":null,"orgAddress":null,"txUrl":"https://explore.veforge.com/transactions/","userAddressName":null,"withdrawFeeRate":0.001,"confirmationCount":12,"infoUrl":null,"enable":true,"name":"Vechain","tradePrecision":8,"depositRemark":null,"enableWithdraw":true,"enableDeposit":true,"coin":"VET"}]} 
		#for item in value2['data']:
		#	pprint(item["symbol"])
		return str([item["coin"] for item in value2['data']])
	
	return content