from company import co
def company():
	f=co.company()
	print("Welcome to our company"+
		"Want to know the details,Here are the available options----"+
		"1.Name\n2.Description\n3.Banch details\n4.Number of employees\n5.Clients\n6.Average profit")
	n=input("enter your option: ")
	if (n==1):
		f.name()
	elif(n==2):
		f.description()
	elif(n==3):
		f.branches()
	elif(n==4):
		f.emp_count()
	elif(n==5):
		f.clients()
	elif(n==6):
		f.profits()
