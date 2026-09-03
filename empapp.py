from employee import Employee

print("welcome to EMP Application")

emp=Employee()
eid=121
while True:
    choice=int(input('''enter your choice 1. add new employee 2. update salary 3. update experience 4. get employee  5. exit'''))
    if choice==1:
        eid+=1
        name=input("enter name:")
        salary=float(input("enter salary"))
        exp=int(input("enter exp"))
        emp.setEmployeeDetails(eid,name,salary,exp)
        
    elif choice==2:
        while True:
            Grade=input("Enter grade 1.A 2.B 3.C 4.others")
            if Grade=="A":
                increment=7
            elif Grade=="B":
                increment=5
            elif Grade=="c":
                increment=3
            else:
                increment=1.5
            print(emp.updatesal(increment))
            break
        increment=int(input("enter a increment "))
        print(emp.updatesal(increment))

    elif choice==3:
        year=int(input("enter ur experience"))
        print("new experience ",emp.newexp(year))

    
    elif choice==4:
        print(emp.getEmployee())

    elif choice==5:
        print("end of application")
    
        break
    else:
        print("wrong choice")
    
