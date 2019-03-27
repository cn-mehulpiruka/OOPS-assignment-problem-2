import client as c

choice=1
while choice >0 and choice<10:
	print("Welcome to Client dashboard")
	print("===="*5)
	print('What to you want to do?')
	print(" 1) Add Client \n 2) View Client \n 3) Show Amount \n 4) Publish \n 5) Go Back")
	choice=int(input())
	if choice>5 or choice<1:
		print("Choose a valid option:")
	if choice==1:
		print("1) Add as a Publisher \n2) Add as a Advertiser")
		choice_add=int(input())
		if choice_add==1:
			print(dir(c.publisher))
		else:
			print(dir(c.advertiser))
	elif choice==5:
		exit()

