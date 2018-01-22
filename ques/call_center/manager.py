from employee import Employee;

class Manager(Employee):
    def __init__(self,name,pay,employees=None):
        Employee.super().__init__(name,email,pay);
        
        if(employees==None):
            self.employees=[];
        else:
            self.employees=employees;
    
