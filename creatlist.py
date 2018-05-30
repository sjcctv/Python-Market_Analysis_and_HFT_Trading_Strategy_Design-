import gdax
import datetime
import exceptions
import time,pytz
import pandas as pd


def creatlist_test(pair,start,end,granularity,rolling):
	public_client = gdax.PublicClient()
	date_format = "%Y-%m-%d %H:%M:%S"
	end=datetime.datetime.strptime(end, date_format)
	diff=end-datetime.datetime.strptime(start, date_format) 
	n_hour=int(round((diff.total_seconds()/3600),0))  #find out how many loop it should run
	start= datetime.datetime.strptime(start, date_format)
	add_1h=datetime.timedelta(hours=1)
	end=start+add_1h   #assign the first end time
	lable=['time','low','high','open','close','volume ']
	l=pd.DataFrame(columns=lable)
	while True:
		k=public_client.get_product_historic_rates(pair,start=str(start),end=str(end),granularity=granularity)
		try:
			count
		except:
			count=1
		else:
			if count>n_hour:
				l=l.reset_index(drop='T') #reindex the value 
				l=l[::-1].reset_index(drop='T')
				l['mva'] = pd.rolling_mean(l['high'],rolling)
			# 	l['mva'] = l['high'].rolling(rolling).mean()
				l['diff']=(l.high-l.mva)/l.high
				return l ##return value
				break
			else:
				print (count,n_hour)   #here  is the only different between creatlist_test and creatlist
				if len(k)>2:
					lable=['time','low','high','open','close','volume ']
					df=pd.DataFrame(k,columns = lable)
					list=[]
					for i in range(0,len(df['time'])):
						list.append((datetime.datetime.utcfromtimestamp(int(df['time'][i])).strftime('%Y-%m-%d %H:%M:%S')))
					df['time']=pd.DataFrame(list)
					l=df.append(l)
					start=start+add_1h
					end=end+add_1h
					n=0  #give each loop 6 chance to obtain the value
					time.sleep(0.5)
					try:
						count
					except:
						count=1
					else:
						count=count+1
				elif len(k)<2 or len(k)==0:
					try:
						n
					except:
						n=0
					else:
							if n<6:
								n=n+1
								time.sleep(1)
								print n
								if n>=3:
									time.sleep(5)
									if  n>=6:
										print start
										print k
										lable=['time','low','high','open','close','volume ']
										df=pd.DataFrame(columns = lable)
										start=start+add_1h
										end=end+add_1h
										n=0
										try:
											count
										except:
											count=1
										else:
											count=count+1

def creatlist(pair,start,end,granularity):
	public_client = gdax.PublicClient()
	date_format = "%Y-%m-%d %H:%M:%S"
	end=datetime.datetime.strptime(end, date_format)
	diff=end-datetime.datetime.strptime(start, date_format)
	n_hour=int(round((diff.total_seconds()/3600),0))
	start= datetime.datetime.strptime(start, date_format)
	add_1h=datetime.timedelta(hours=1)
	end=start+add_1h
	lable=['time','low','high','open','close','volume ']
	l=pd.DataFrame(columns=lable)
	while True:
		k=public_client.get_product_historic_rates(pair,start=str(start),end=str(end),granularity=granularity)
		try:
			count
		except:
			count=1
		else:
			if count>n_hour:
				l=l.reset_index(drop='T') #reindex the value 
				return l ##return value
				break
			else:
# 				print (count,n_hour)
				if len(k)>2:
					lable=['time','low','high','open','close','volume ']
					df=pd.DataFrame(k,columns = lable)
					list=[]
					for i in range(0,len(df['time'])):
						list.append((datetime.datetime.utcfromtimestamp(int(df['time'][i])).strftime('%Y-%m-%d %H:%M:%S')))
					df['time']=pd.DataFrame(list)
					l=df.append(l)
					start=start+add_1h
					end=end+add_1h
					n=0  #give each loop 6 chance to obtain the value
					time.sleep(0.6)
					try:
						count
					except:
						count=1
					else:
						count=count+1
				elif len(k)<2 or len(k)==0:
					try:
						n
					except:
						n=0
					else:
							if n<6:
								n=n+1
								time.sleep(1)
								if n>=3:
									time.sleep(5)
									if  n>=6:
										print start
										print k
										lable=['time','low','high','open','close','volume ']
										df=pd.DataFrame(columns = lable)
										start=start+add_1h
										end=end+add_1h
										n=0
										try:
											count
										except:
											count=1
										else:
											count=count+1