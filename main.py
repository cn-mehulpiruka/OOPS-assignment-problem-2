import employer as emp
def Employer():
    n = int(input("enter the users"))
    for i in range(0,n):
        choice = int(input("enter the choice"))
        if (choice == 1):
            emp1 = emp.Employer('empid', 'name' ,'age','gender', 'email', 'contact_no', 'alt_no', 'designation', 'branch', 'team_manager')
            emp1.set_empid(input("enter the empid:"))
            emp1.set_name(input("enter the name: "))
            emp1.set_age(input("enter the age:"))
            emp1.set_gender(input("enter the gender:"))
            emp1.set_email(input("enetr the email:"))
            emp1.set_contact_no(input("enter the contact number:"))
            emp1.set_alt_no(input("enter the alternate number:"))
            emp1.set_designation(input("enter the designation:"))
            emp1.set_branch(input("enter the branch:"))
            emp1.set_team_manager(input("enter the team manager:"))
            print()
            print("the details you entered are:")
            print(emp1)
        if (choice == 2):
            traine = emp.Trainee('empid', 'name' ,'age','gender', 'email', 'contact_no', 'alt_no', 'designation', 'branch', 'team_manager','stifend','duration')
            traine.set_empid(input("enter the empid:"))
            traine.set_name(input("enter the name: "))
            traine.set_age(input("enter the age:"))
            traine.set_gender(input("enter the gender:"))
            traine.set_email(input("enetr the email:"))
            traine.set_contact_no(input("enter the contact number:"))
            traine.set_alt_no(input("enter the alternate number:"))
            traine.set_designation(input("enter the designation:"))
            traine.set_branch(input("enter the branch:"))
            traine.set_team_manager(input("enter the team manager:"))
            traine.set_stifend(input("enter stifend:"))
            traine.set_duration(input("enter the duration:"))
            print()
            print("the details you entered are:")
            print(traine)
        if(choice == 3):
            permanent_employee = emp.permanent('empid', 'name' ,'age','gender', 'email', 'contact_no', 'alt_no', 'designation', 'branch', 'team_manager', 'salary', 'contract_duration')
            permanent_employee.set_empid(input("enter the empid:"))
            permanent_employee.set_name(input("enter the name: "))
            permanent_employee.set_age(input("enter the age:"))
            permanent_employee.set_gender(input("enter the gender:"))
            permanent_employee.set_email(input("enetr the email:"))
            permanent_employee.set_contact_no(input("enter the contact number:"))
            permanent_employee.set_alt_no(input("enter the alternate number:"))
            permanent_employee.set_designation(input("enter the designation:"))
            permanent_employee.set_branch(input("enter the branch:"))
            permanent_employee.set_team_manager(input("enter the team manager:"))
            permanent_employee.set_salary(input("enter the salary:"))
            permanent_employee.set_contract_duration(input("enter the contract duration:"))
            print()
            print("the details you entered are:")
            print(permanent_employee)
        if(choice == 4):
            Department = emp.department('depname','depid','project_id')
            Department.set_depname(input("enter the department name:"))
            Department.set_depid(input("enter the department ID:"))
            Department.set_project_id(input("enter project_id:"))
            print()
            print("the details you entered are:")
            print(Department)
main()
