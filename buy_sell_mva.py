import exceptions
import gdax
import datetime
import json
import time,pytz
import pandas as pd
import creatlist
import mva


creatlist=creatlist.creatlist
ma_earning_trade=mva.ma_earning_trade

	
def trade_ma(pair,size,h,granularity,fee,tl,slmm,price,n_coin,rolling,k_b,k_s,key,b64secret,passphrase):
	pass
	date_format = "%Y-%m-%d %H:%M:%S"
	start_time=str(datetime.datetime.utcnow().strftime(date_format))
	while True:
		try:
			result
		except:
			stop_lost=0  #set stop_lost as zero for the first loop
			result=ma_earning_trade(pair,size,h,granularity,fee,tl,slmm,price,n_coin,rolling,k_b,k_s,stop_lost,start_time,key,b64secret,passphrase) #the first result form the loop
			earning=result[1] #get value from the first loop
			price=result[0]            ##get value from the first loop   
			n_coin=result[2]         ##get value from the first loop
			stop_lost=result[5]
			print (earning,price,n_coin,stop_lost)  #print the result
			print start_time 
			time.sleep(30)   #sleep after the first loop
		else:
			try:
				result=ma_earning_trade(pair,size,h,granularity,fee,tl,slmm,price,n_coin,rolling,k_b,k_s,stop_lost,start_time,key,b64secret,passphrase)
				earning=earning+result[1] #get value from the result
				price=result[0]            ##get value from the result 
				n_coin=result[2]         ##get value from the result
				stop_lost=result[5]+stop_lost
			except Exception,e:
				print e
				print 'error happened and restarted at %s' % (datetime.datetime.utcnow())
				continue
			print (earning,price,n_coin,stop_lost)
			print start_time
			time.sleep(30)

pair='BTC-USD'
h=2   #must bigger than granularity/60
granularity=60
fee=0.003
price=1  # can not be zero!!!
n_coin=0
rolling=100
size=0.001
k_b=0.047
k_s=0.025
tl=11
slmm=1000
