import gdax 
import time





def buy(pair,size,buy_price,key,b64secret,passphrase):
	auth_client = gdax.AuthenticatedClient(key, b64secret, passphrase)
	buy=auth_client.buy(price=buy_price, #place sale order
        		size=size, #BTC
        		product_id=pair)
	if len(buy)>2:
		k=buy['id']
		n=0
		while True:
			if auth_client.get_order(k)['status']=='done':
				return auth_client.get_order(k)['fill_fees']
				break
			elif auth_client.get_order(k)['status']!='done':
				if n<5:
					n=n+1
					print n
					time.sleep(60)
				elif n>=5:
					return 'cancel'
					break	
	else:
		print buy  #show any error message

def sell(pair,size,sell_price,key,b64secret,passphrase):
	auth_client = gdax.AuthenticatedClient(key, b64secret, passphrase)
	sell=auth_client.sell(price=sell_price, #place sale order
                size=size, #BTC
                product_id=pair)
	if len(sell)>2:
		k=sell['id']
		n=0
		while True:
			if auth_client.get_order(k)['status']=='done':
				return auth_client.get_order(k)['fill_fees']
				break
			elif auth_client.get_order(k)['status']!='done':
				if n<5:
					n=n+1
					print n
					time.sleep(60)
				elif n>=5:
					return 'cancel'
					break	
	else:  
		print sell   #show any error message
