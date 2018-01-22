class Employee(object):
    def __init__(self,firstname,lastname,pay,level):
        self.firstname=firstname;
        self.lastname=lastname;
        self.pay=pay;
        self.have_call=False;
        self.level=level;
    @property
    def fullname(self):
        return "Name:{} {}, Email:{}".format(self.lastname,self.lastname,self.email);
    
    def assign_call(self):
        self.have_call=True;
    
    def revoke_call(self):
        self.have_call=False;
    @property
    def email(self):
        return self.firstname + "." + self.lastname + "@email.com";


# emp1=Employee("ravi","guru",10000,1);
# print(emp1.email);
# print(emp1.fullname);