import client as c

choice=1

Advertiser=[]
Publisher=[]

def create_client():
		print("1) Add as a Publisher \n2) Add as a Advertiser")
		choice_add=int(input())
		name_=input("Enter Name of the CLient")
		flight_period_=int(input("Enter the flight period of the Client"))
		print("Choose a Tax Exntity\n 1) Coporate \n 2) Indiviual")
		tax_entity_= "Coporate" if input()==1 else "Indiviual"
		tax_id_no_=input("Enter a Tax No") 
		if choice_add==1:
			url_=input("Enter url of the Client")
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
	pass
def create_order():
	pass
def create_inventory():
	pass
def show_amoutn(client):
	pass
def go_back():
	pass

while choice >0 and choice<10:
	print("===="*7)
	print("\nWelcome to Client dashboard")
	print("===="*7)
	print('What to you want to do?')
	print(" 1) Add Client \n 2) View Client \n 3) Show Amount \n 4) Publish \n 5) Add addons \n 6) Go Back")
	choice=int(input())
	if choice>5 or choice<1:
		print("Choose a valid option:")
	elif choice==1:
		create_client()
	elif choice==4:
		publish()
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
	elif choice==6:
		exit()


