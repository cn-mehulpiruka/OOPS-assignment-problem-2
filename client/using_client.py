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

def view_clients():
	pass
def view_client(c.client):
	pass
def publish():
	pass
def show_amoutn(c.client):
	pass
def go_back():
	pass
while choice >0 and choice<10:
	print("Welcome to Client dashboard")
	print("===="*5)
	print('What to you want to do?')
	print(" 1) Add Client \n 2) View Client \n 3) Show Amount \n 4) Publish \n 5) Go Back")
	choice=int(input())
	if choice>5 or choice<1:
		print("Choose a valid option:")
	if choice==1:
		create_client()
	if choice==2:
		print("1) View All CLinets\n2) View Publisher\n 3) View Advertisers")
		ch=int(input())
		if ch==1:
			view_clients(Publisher,Advertisers)
		view_clients()
	elif choice==5:
		exit()


