import os
import client.client as cl
import company.test as co
import employer.main as e
def welcome():
	ch=int(input("1) Company \n2) Employees\n3) Client \n4) Exit\n  :"))
	if ch==1:
		co.company()
		pass
	elif ch==2:
		
		pass
	elif ch==3:
		print("Reaady to go with the client dashboard??? ")
		# print(dir(c))
		cl.client_working()
	else:
		exit()

if __name__=='__main__':
	if os.name=='posix':
		os.system('clear')
	print("=**="*50)
	print("=**="*50)
	print("=**="*20,"Welcome to the trainees made project ","=**="*20)
	print("=**="*50)
	print("=**="*50)
	welcome()