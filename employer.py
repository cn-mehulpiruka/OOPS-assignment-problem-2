class Employer:
	def __init__(self):
		self.empid = ''
		self.name = ''
		self.age = ''
		self.gender = ''
		self.email = ''
		self.contact_no = ''
		self.alt_no = ''
		self.designation = ''
		self.branch = ''
		self.team_manager = ''		
	def set_empid(self, empid):
		self.empid = empid
		
	def set_name(self, name):
		self.name = name
		
	def set_age(self, age):
		self.age = age
		
	def set_gender(self, gender):
		self.gender = gender
		
	def set_email(self, email):
		self.email = email
		
	def set_contact_no(self, contact_no):
		self.contact_no = contact_no
		
	def set_alt_no(self, alt_no):
		self.alt_no = alt_no
		
	def set_designation(self, designation):
		self.designation = designation
		
	def set_branch(self, branch):
		self.branch = branch
		
	def set_team_manager(self, team_manager):
		self.team_manager = team_manager
		
	def get_empid(self):
		return self.empid
		
	def get_name(self):
		return self.name
		
	def get_age(self):
		return self.age 
		
	def get_gender(self):
		return self.gender
		
	def get_email(self):
		return self.email
		
	def get_contact_no(self):
		return self.contact_no
		
	def get_alt_no(self):
		return self.alt_no
		
	def get_designation(self):
		return self.designation
		
	def get_branch(self):
		return self.branch
		
	def get_team_manager(self):
		return self.team_manager
		
	def __str__(self):
	    return 'EmpID: '   +   self.empid  +   \
               '\nName: '   +   self.name   +   \
               '\nAge: '    +   self.age    +   \
               '\nGender: ' +   self.gender +   \
               '\nEmail: '  +   self.email  +   \
               '\nContact No.: '    +   self.contact_no +   \
               '\nAlt no.: '    +   self.alt_no +   \
               '\nDesignation: '    + self.designation  +   \
               '\nBranch: ' +   self.branch +   \
               '\nTeam Manager: '   +   self.team_manager   +   \
               '\nSalary: ' +   self.salary
class Trainee(Employer):
	def __init__(self,stifend,duration):
		super().__init__()
		self.stifend = stifend
		self.duration = duration
	def set_stifend(self,stifend):
		self.stifend = stifend
	def set_duration(self,duration):
		self.duration = duration
	def get_stifend(self):
		return self.stifend
	def get_duration(self):
		return self.duration
	def __str__(self):
	    return 'stifend: '   +   self.stifend  +   \
               '\nduration: '   +   self.duration
class permanent(Employer):
	def __init__(self,salary,contract):
		super().__init__()
		self.salary = salary
		self.contract = contract
	def set_salary(self,salary):
		self.salary = salary
	def set_contract(self,contract):
		self.contract = contract
	def get_salary(self):
		return self.salary
	def get_contract(self):
		return self.contract
	def __str__(self):
	    return 'salary: '   +   self.salary +   \
              '\ncontract: '   +   self.contract
class Hr_management(Employer):
	def __init__(self,num_of_recruitment,finance_description):
		super().__init__()
		self.num_of_recruitment = num_of_recruitment
		self.finance_descriptiom = finance_description
	def set_num_of_recruitment(self,num_of_recruitment):
		self.num_of_recruitment = num_of_recruitment
	def set_finance_description(self,finance_description):
		self.finance_description = finance_description
	def get_num_of_recruitment(self):
		return num_of_recruitment
	def get_finance_description(self):
		return finance_description
	def __str__(self):
	    return 'num_of_recruitment: '   +   self.num_of_recruitment +   \
               '\nfinance_description: '   +   self.
class department:
	def __init__(self,depname,depid,project_id):
		self.depname = depname
		self.depid = depid
		self.project_name = project_name
	def set_depname(self,depname):
		self.depname = depname
	def set_depid(self,depid):
		self.depid = depid
	def set_project_id(self,project_id):
		self.project_id = project_id
	def get_depname(self):
		return self.depname
	def get_depid(self):
		return self.depid
	def get_project_id(self):
		return self.project_id
	def __str__(self):
	    return 'depname: '   +   self.depname  +   \
               '\ndepid: '   +   self.depid   +   \
               '\nproject_id: '    +   self.project_id 

          
		
