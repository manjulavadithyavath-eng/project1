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
        self.salary=self.salary+self.salary*percentage
        return self.salary


    def newexp(self,year):
        self.exp=self.exp+year
        return self.exp
        
