class employee:
    raise_amount=1.10;
    def __init__(self,first_name,middle_name,last_name,salary):
        self.first_name=first_name;
        self.middle_name=middle_name;
        self.last_name=last_name;
        self.salary=salary;
    def fullname(self):
        print("{} {} {}".format(self.first_name,self.middle_name,self,last_name));
    
    def raise_amount_method(self):
        print("Employee Total Salary:",self.salary*self.raise_amount);



emp1=employee("ravi","kumar","guru",200000);
emp2=employee("sunil","kumar","raghav",50000);
emp1.raise_amount=1.25;
print(emp1.__dict__);
emp1.raise_amount_method();
emp2.raise_amount_method();