import sys;
import datetime;
class employee:
    raise_amount=1.10;
    no_of_employee=0;
    def __init__(self,first_name,middle_name,last_name,salary):
        self.first_name=first_name;
        self.middle_name=middle_name;
        self.last_name=last_name;
        self.salary=salary;
        employee.no_of_employee+=1;

    def fullname(self):
        print('{} {} {} {}'.format(self.first_name,self.middle_name,self.last_name,self.salary));
    
    def apply_raise(self):
        print("total raise amount:",round(self.salary*self.raise_amount,2));

    @classmethod
    def set_raise_amount(cls,raise_amount):
        cls.raise_amount=raise_amount;
    
    @classmethod
    def number_of_employee(cls):
        print("Total number of employee in your organization:",cls.no_of_employee);

    @classmethod
    def string_formatter(cls,emp_string):
        first_name,middle_name,last_name,salary=emp_string.split("-");
        return employee(first_name,middle_name,last_name,salary);
    @staticmethod
    def is_work_day(day):
        if(day.weekday()==6 or day.weekday()==5):
            return False;
        return True;
    

date=datetime.date(2018,1,22);
print(employee.is_work_day(date));

