import datetime as d
today = d.date.today()
class client:
	_client_id=0
	def __init__(self):
		client._client_id+=1
		self._client_id=client._client_id
		self.name=None
		self.client_type=None
		self.tax_entity=None
		self.tax_id_no=None
		self.total_amountbilled=0
	@classmethod
	def billing(cls,inventory,order):
		sdate_=d.date(int(order.start_date[0:4]),int(order.start_date[5:7]),int(order.start_date[8:]))
		edate_=d.date(int(order.end_date[0:4]),int(order.end_date[5:7]),int(order.end_date[8:]))
		print(edate_- sdate_)
		time_period=int((str(edate_- sdate_).split(" "))[0])
		if order.billing_period=='Day':
			return order.amountpaid*time_period
		elif order.billing_period=='Monthly':
			return (order.amountpaid//30)*time_period
		else:
			return (order.amountpaid//365)*time_period

	@classmethod
	def publish(cls,publishers,advertiser):
		if len(advertiser.orders) == 0:
			print("No orders their for the Advertiser")
			return 
		for order in advertiser.orders:
			flag=False
			sdate_=d.date(int(order.start_date[0:4]),int(order.start_date[5:7]),int(order.start_date[8:]))
			edate_=d.date(int(order.end_date[0:4]),int(order.end_date[5:7]),int(order.end_date[8:]))
			if sdate_<=today and today<=edate_ and order.status==True:
				for publisher in publishers:
					if len(publisher.inventories)==0:
						break
					for inventory in publisher.inventories:
						print(inventory.price," ",order.amountpaid)
						if float(inventory.price)<float(order.amountpaid) and inventory.status==True:
						 	print("Published")
						 	amount=client.billing(inventory,order)
						 	publisher.earned(amount)
						 	advertiser.spent(amount)
						 	inventory.status=False
						 	order.status=False
						 	flag=True
						 	break
					if flag:
				 		break
			if not flag:
	 			print("Sorry no publisher avaiable now")

class publisher(client):
	__publisher_id=0
	def __init__(self):
		super().__init__()
		print((self._client_id))
		publisher.__publisher_id+=1
		self.__publisher_id=publisher.__publisher_id
		self.url=None
		# self.total_amountbilled=0
		self.orders_serving=[]
		self.flight_period=1
		self.inventories=[]
	def create_publisher(self,url_,flight_period_,name_,tax_entity_="Coporate",tax_id_no_=None):
		self.name=name_

		if tax_entity_=='Coporate':
			print(tax_entity_)
			# print("")
		else:
			tax_entity='Indiviual'
		self.tax_id_no=tax_id_no_
		self.client_type="Publisher"
		self.url=url_
		self.flight_period=flight_period_
	def create_inventory(self,size_,price_,status_):
		new_invent=inventory.create_new_inventory(size_,price_,status_)
		self.inventories.append(new_invent)
	def earned(self,amount_):
		print("earned",self)
		self.total_amountbilled+=amount_


class inventory:
	_inventory_id=0
	def __init__(self):
		inventory._inventory_id+=1
		self._inventory_id=inventory._inventory_id
		self.size_=0
		self.price=1.04
		self.status=True
	@classmethod
	def create_new_inventory(cls,size_,price_,status_=True):
		new_invent=inventory()
		new_invent.size=size_
		new_invent.price=price_
		new_invent.status=status_
		return new_invent




class advertiser(client):
	__advertiser_id=0
	def __init__(self):
		super().__init__()
		advertiser.__advertiser_id+=1
		self.__advertiser_id=advertiser.__advertiser_id
		self.flight_period=0
		# self.total_amountbilled=0
		self.orders=[]
	
	def create_advertiser(self,name_,flight_period_=1,tax_entity_="Coporate",tax_id_no_=None):
		self.name=name_
		print(tax_entity_)

		if tax_entity_=='Coporate':
			# company=company()
			print(tax_entity_)

		else:
			tax_entity='Indiviual'
		self.tax_entity=tax_entity_
		self.tax_id_no=tax_id_no_
		self.client_type="Advertiser"
		self.flight_period=flight_period_

	def create_ad(self,start_date_,end_date_,amountpaid_,billing_period_,status_=False):
		new_order=order()
		new_order.create_order(self.__advertiser_id,start_date_,end_date_,status_,amountpaid_,billing_period_)
		self.orders.append(new_order)
	def spent(self,amount_):
		print("spend",self)
		self.total_amountbilled+=amount_

class order:
	__order_id=0
	def __init__(self):
		order.__order_id+=1
		self.__order_id=order.__order_id
		self.start_date=str(today.year)+"-"+str(today.month)+"-"+str(today.day)
		self.end_date=str(today.year)+"-"+str(today.month)+"-"+str(today.day+1)
		self.status=False
		self.amountpaid=0
		self.billing_period="Day"
		self.advertiser_id=None
	def create_order(self,advertiser_id_,start_date_,end_date_,status_=True,amountpaid_=1.05,billing_period_="Day",):
		self.start_date=start_date_
		self.end_date=end_date_
		self.status=status_
		self.amountpaid=amountpaid_
		self.billing_period=billing_period_
		self.advertiser_id=advertiser_id_




