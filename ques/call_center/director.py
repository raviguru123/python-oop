from employee import Employee;

class Director(Employee):
    def __init__(self,name,pay,employees=None):
        super(Director,self).__init__(name,email,pay);
        if(employees==None):
            self.employees=[];
        else:
            self.employees=employees;
