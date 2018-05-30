import exceptions
import gdax
import datetime
import json
import time,pytz
import pandas as pd
import multiprocessing as mp
import creatlist as cl
import mva



creatlist_test=cl.creatlist_test
ma_earning_test=mva.ma_earning_test


start='2018-05-01 06:00:00'
date_format = "%Y-%m-%d %H:%M:%S"
now=str(datetime.datetime.utcnow().strftime(date_format))
end=now
price=99999
pair='BTC-USD'
h=2   #not needed in the test mode
granularity=60
fee=0.003
price=99999
size=0.01
n_coin=0
rolling=100
k_b=0.031
k_s=0.016
tl=11
slti=1000


try:
 pd.read_csv("data_BTC_05_01_18.csv")
except:
	while True:
		try:
			m=creatlist_test(pair,start,end,granularity,rolling)
			m.to_csv('data_BTC_05_01_18.csv', sep=',', encoding='utf-8')
			break 
		except Exception,e:
			print e
			time.sleep(3)
			continue
else:
	m=pd.read_csv("data_BTC_05_01_18.csv",index_col=0)



# date_format = "%Y-%m-%d %H:%M:%S"
# 	end=datetime.datetime.strptime(end, date_format)
# 	diff=end-datetime.datetime.strptime(start, date_format) 



# # m=m[::-1].reset_index(drop='T')  # test if the market is droping 
# m=creatlist_test(pair,start,end,granularity)

# # print (m['high'][(18984)-1],m['time'][(18984)-1],m['high'][0],m['time'][0])


# print ma_earning_test(m,fee,tl,slti,price,n_coin,rolling,k_b,k_s,show_step=True)

################# #slow raspberry single core
# not updated for a while need works

# list=[]
# for rolling in range(50,300,50):
#        for k_b in range(30,50):
#                for k_s in range(10,30):
# 						for tl in range(4,11):
# 							for slt in range(500,1001,500):
# 								print(rolling,k_b,k_s,tl,slt)
# 								list.append(ma_earning_test(m,fee,tl,slti,price,n_coin,rolling,k_b*0.001,k_s*0.001))

# lable=['earning','mv','diff_b','diff_s','n_of_trade']
# df=pd.DataFrame(list,columns = lable)
# print df.loc[df['earning'].idxmax()]
# df.to_csv('MMVA_12_21.csv', sep=',', encoding='utf-8')


# mutil core
result_list =[]
print 'multiprocessing'
print mp.cpu_count()
def log_result(result):
    # This is called whenever foo_pool(i) returns a result.
    # result_list is modified only by the main process, not the pool workers.
    result_list.append(result)

def apply_async_with_callback():
	strat=datetime.datetime.now()
	pool = mp.Pool(mp.cpu_count()-2)
	for rolling in range(100,101):
		for k_b in range(21,31):
			for k_s in range(10,20):
				for tl in range(11,12):
					for slti in range(1000,1001):
						pool.apply_async(ma_earning_test, args = (m,fee,tl,slti,price,n_coin,rolling,k_b*0.001,k_s*0.001), callback = log_result)
	pool.close()
	pool.join()
	lable=['earning','mv','diff_b','diff_s','n_of_trade','tollrance','max_lost','slt']
	df=pd.DataFrame(result_list,columns = lable)
	df.to_csv('res_BTC.csv', sep=',', encoding='utf-8')
	end=datetime.datetime.utcnow()
	print df.loc[df['earning'].idxmax()]
	print (datetime.datetime.now()-strat)

if __name__ == '__main__':
    apply_async_with_callback()





