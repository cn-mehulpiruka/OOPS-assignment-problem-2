class Employer:
    def __init__(self,empid,name,age,gender,email,contact_no,alt_no,designation,branch,team_manager):
        self.empid = empid
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email
        self.contact_no = contact_no
        self.alt_no = alt_no
        self.designation = designation
        self.branch = branch
        self.team_manager = team_manager        
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
               '\nTeam Manager: '   +   self.team_manager
class Trainee(Employer):
    def __init__(self,empid,name,age,gender,email,contact_no,alt_no,designation,branch,team_manager,stifend,duration):
        super().__init__(empid,name,age,gender,email,contact_no,alt_no,designation,branch,team_manager)
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
    def __init__(self,empid,name,age,gender,email,contact_no,alt_no,designation,branch,team_manager,salary,contract_duration):
        super().__init__(empid,name,age,gender,email,contact_no,alt_no,designation,branch,team_manager)
        self.salary = salary
        self.contract = contract_duration
    def set_salary(self,salary):
        self.salary = salary
    def set_contract_duration(self,contract_duration):
        self.contract_duration = contract_duration
    def get_salary(self):
        return self.salary
    def get_contract_duration(self):
        return self.contract_duration
    def __str__(self):
        return 'salary: '   +   self.salary +   \
              '\ncontract: '   +   self.contract
class department:
    def __init__(self,depname,depid,project_id):
        self.depname = depname
        self.depid = depid
        self.project_id = project_id
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

