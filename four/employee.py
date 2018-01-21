class Employee(object):
    raise_inc=1.05;
    def __init__(self,first_name,middle_name,last_name,pay):
        self.first_name=first_name;
        self.middle_name=middle_name;
        self.last_name=last_name;
        self.pay=pay;
    
    def fullname(self):
        print("{} {} {} :Salray=  {}".format(self.first_name,self.middle_name,self.last_name,self.pay));

    def apply_raise(self):
        self.pay=self.pay*self.raise_inc;
        
    def get_pay(self):
        return self.pay;

    @classmethod
    def set_raise_amount(cls,raise_amount):
        cls.raise_amount=raise_amount;
      
