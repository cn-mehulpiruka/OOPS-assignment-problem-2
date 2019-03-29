import client_dict as c
import datetime as d
Advertiser=[]
Publisher=[]


def create_client():
		print("1) Add as a Publisher \n2) Add as a Advertiser ")
		choice_add=int(input())
		name_=input("Enter Name of the CLient ")
		flight_period_=int(input("Enter the flight period of the Client "))
		print("Choose a Tax Exntity\n 1) Coporate \n 2) Indiviual")
		tax_entity_= "Coporate" if input()==1 else "Indiviual"
		tax_id_no_=input("Enter a Tax No ") 
		if choice_add==1:
			url_=input("Enter url of the Client ")
			p=c.publisher()
			p.create_publisher(url_,flight_period_,name_,tax_entity_,tax_id_no_)
			print(dir(c.publisher))
			Publisher.append(p)
			print(len(Publisher))

		else:
			print(dir(c.advertiser))
			a=c.advertiser()
			a.create_advertiser(name_,flight_period_,tax_entity_,tax_id_no_)
			Advertiser.append(a)
			print(len(Advertiser))

def view_clients(clients):

	keys=list(clients[0].__dict__.keys())
	print(keys, sep='\t', end='\n', flush=True) 
	print("=+=+=+=+=+=+="*len(keys))
	for client in clients:
		view_client(client)

def view_client(client):
	values=list(client.__dict__.values())
	print(values, sep='\t\t', end='\n\n', flush=True) 

	pass
def publish():
	print("Advertiser ID\t\t Advertiser Name")
	cnt=1
	for advertiser in Advertiser:
			print(cnt,"\t\t",advertiser.name)
			cnt+=1

	ch=input("\n Want to publish all orders of?(yes/no)")
	if ch=="yes" or ch=="Yes" or ch=="1":
		for advertiser in Advertiser:
			c.client.publish(Publisher, advertiser)
	else :
		publish_advertiser_id=int(input("Enter The advertiser id to publish: "))
		# print(Advertiser[publish_advertiser_id-1])
		c.client.publish(Publisher,Advertiser[publish_advertiser_id-1])
def create_addons():
	ch=int(input("What do want to create ?\n 1) Inventory \n 2) Order"))
	if ch==1:
		create_inventory()
	elif ch==2:
		create_order()
	else:
		print("Wrong options..!! Starting again..!!")
	
def create_order():
	print("Advertiser ID\t\t Advertiser Name")
	cnt=1
	for advertiser in Advertiser:
			print(cnt,"\t\t",advertiser.name)
			cnt+=1
	advertiser_id=int(input("Enter The advertiser id for which you want to create order: "))
	order_4_advertiser= (Advertiser[advertiser_id-1])
	start_date_=input("Enter start date for the order : (press 1 for today) (YYYY-MM-DD)")
	if start_date_=="1":
		start_date_=str(today)
	print(start_date_)

	end_date_=input("Enter end date for the order: (YYYY-MM-DD):  ")
	amountpaid_=float(input("Enter amount advertiser would be paying : (enter amount in 00.00): "))
	ch=(input("Choose your desire billing period\n 1) Day \n 2) Monthly \n 3) Annually: \n"))
	billing_period_= "Day" if  ch== "1" else  ("Monthly" if ch=="2" else "Annually" )
	print(billing_period_)
	if start_date_!= today and d.date(int(start_date_[0:4]),int(start_date_[5:7]),int(start_date_[8:]))< today:
		status_=True
	else:
		status_=False

	order_4_advertiser.create_ad(start_date_,end_date_,amountpaid_,billing_period_,status_)
	print(order_4_advertiser.__dict__)

def create_inventory():
	print("Publishers ID\t\t Publishers Name")
	cnt=1
	for publisher in Publisher:
			print(cnt,"\t\t",publisher.name)
			cnt+=1
	publisher_id=int(input("Enter The publisher id for which you want to create Inventory: "))
	inventory_of_publisher= (Publisher[publisher_id-1])
	size_=input("Enter size in x * Y format: ")
	price_=input("Enter price you are excepting: ")
	inventory_of_publisher.create_inventory(size_,price_,True)
	print(inventory_of_publisher.__dict__)

def show_amoutn():
	ch=int(input("\nChoose the client whose you want to see the amount\n1) Publishers\n2) Advertisers \n3) All\n"))
	cnt=1
	if ch==1 or ch==3:
		print("Publishers ID\t\t Publishers Name")
		for publisher in Publisher:
				print(cnt,"\t\t",publisher.name)
				cnt+=1
	if ch==2 or ch==3:
		print("Advertiser ID\t\t Advertiser Name")
		for advertiser in Advertiser:
				print(cnt,"\t\t",advertiser.name)
				cnt+=1
	
	cnt=1
	if ch==3:
		print("Publishers ID\t\t Publishers Name")
		for publisher in Publisher:
				print(cnt,"\t\t",publisher.name,"\t\t",publisher.total_amountbilled)
				cnt+=1
		print("Advertiser ID\t\t Advertiser Name\t\t")
		for advertiser in Advertiser:
				print(cnt,"\t\t",advertiser.name,"\t\t",advertiser.total_amountbilled)
				cnt+=1
	else:
		client_id=int(input("Enter the no corespondingto the client "))
		if ch==1:
			obj=Publisher[client_id-1]
		else:
			obj=Advertiser[client_id-1]
		print("Total Amount: ",obj.total_amountbilled)



def go_back():
	pass


def client_working():
	today = d.date.today()
	choice=1
	while choice >0 and choice<10:
		print("===="*7)
		print("\nWelcome to Client dashboard")
		print("===="*7)
		print('What to you want to do?')
		print(" 1) Add Client \n 2) View Client \n 3) Show Amount \n 4) Publish \n 5) Add addons \n 6) Go Back")
		choice=int(input())
		if choice>6 or choice<1:
			print("Choose a valid option:")
		elif choice==1:
			create_client()
		
		elif choice==2:
			print("1) View All CLinets\n2) View Publisher\n3) View Advertisers")
			ch=int(input())
			if ch==1 or ch==3:
				print("All Advertisers")
				if len(Advertiser)<1:
					print ("===No Advertisers.!! Get some==\n")
				else:
					view_clients(Advertiser)
			if ch==1 or ch==2:
				print("All Publishers")
				if len(Publisher)<1:
					print ("===No Publishers.!! Get some===\n")
				else:
					view_clients(Publisher)
		elif choice==3:
			show_amoutn()
		elif choice==4:
			publish()
		elif choice==5:
			create_addons()

		elif choice==6:
			exit()


