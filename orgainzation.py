import os
import client.client as c
  def welcome():
 	ch=int(input("1) Company \n2) Employees\n3) Client \n4) Exit\n  :"))
 	if ch==1:
 		pass
 	elif ch==2:
 		pass
 	elif ch==3:
 		print("Reaady to go with the client dashboard??? ")
 		print(dir(c))
 		c.client_working()
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