class Employee:
    def _init_(self,id,name,salary,exp):
        self.id=0
        self.name=''
        self.salary=0
        self.exp=0

    def setEmployeeDetails(self,id,name,salary,exp):
        self.id=id
        self.name=name
        self.salary=salary
        self.exp=exp
        

    def getEmployee(self):
       return f'Employee Details:\n Id:{self.id}\n Name:{self.name}\n Salary:{self.salary} \n Experience:{self.exp}'

    def updatesal(self,percentage):
        '''
        grade=int(input("enter a grade 1.A 2.B 3.C"))
        if grade==1:
            increment=0.07
        elif grade==2:
            increment=0.05
        elif grade==3:
            increment=0.03
        else:
            increment=0.015'''
        self.salary=self.salary+self.salary*percentage
        return self.salary


    def newexp(self,year):
        self.exp=self.exp+year
        return self.exp
        
       
