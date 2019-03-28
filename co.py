class company:
	def __init__(self):
		self.data = []
		#self.Name=self.name()

	def name(self):
		print("CondeNast")
		return
	def description(self):
		print("Conde Nast Inc operates as a media company.The Company provides publishing products and services."+
			"Conde Nast offers consumer and business-to-business magazine publication services,\n"+
			"as well as websites and applications for mobile and tablet devices.Conde Nast serves customers in the State of New York.\n")
	def branches(self):
		def main_branch():
			print("Address:-\n1 World Trade Center,\nNew York, NY 10007,\n USA\n")
		def contentwriting_branch():
			print("Address:-\n2nd Floor, Darabshaw House, \nShoorji Vallabhdas Marg, Ballard Estate,\n Mumbai 01\n")
		def technical_branch():
			print("Address:-\nRMZ Millenia Business Park, Phase II,\n Perungudi, Chennai, \nTamil Nadu 600096\n")		
		if(branch=='main'):
			main_branch()
		elif(branch=='content'):
			contentwriting_branch()
		elif(branch=='technical'):
			technical_branch()
		else:
			print('sorry..No such branch')
	def emp_count(self):
		import csv
		input_file=open("100 Records.csv")
		reader_file=csv.reader(input_file)
		value=len(list(reader_file)[1:])
		print(value)
	def profits(self):
		import pandas as pd
		data=pd.read_csv('100 Sales Records.csv')
		avg_profit=data['Total Profit'].mean()
		print(avg_profit)
	def clients(self):
		import csv
		input_file=open("100 Records.csv")
		reader_file=csv.reader(input_file)
    		for row in reader_file:
    			print(row[2])
co=company()
co.name()
co.description()
co.emp_count()	
co.profits()
co.clients()
branch=raw_input("main or content or technical\n")
co.branches()

#csvfile.close()
#print(n)



