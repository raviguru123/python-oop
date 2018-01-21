import sys;

class employee:
    def __init__(self,first_name,middle_name,last_name):
        self.first_name=first_name;
        self.middle_name=middle_name;
        self.last_name=last_name;
    def fullname(self):
        print('{} {}'.format(self.first_name,self.middle_name));\

        


emp1=employee("ravi","kumar","guru");
emp2=employee("sunil","kumar","raghav");

# emp1.fullname();
# emp2.fullname();

employee.fullname(emp1);
