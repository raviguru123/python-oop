from employee import Employee

class Manager(Employee):

    def __init__(self,first_name,middle_name,last_name,pay,employeess=None):
        super(Manager,self).__init__(first_name,middle_name,last_name,pay);
        if(employeess==None):
            self.employeess=[];
        else:
            self.employees=employeess;

    def add_employees(self,emp):
        self.employeess.append(emp);
    
    def remove_employees(self,emp):
        self.employeess.remove(emp);
    def list_employees(self):
        for emp in self.employeess:
            emp.fullname();