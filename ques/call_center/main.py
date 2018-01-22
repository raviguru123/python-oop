# from respondent import Respondent;
# from manager import Manager;
# from director import Director;

# class Calling(Respondent,Manager,Director):
#     self __init__(self):
#     print("main function called");


# manager1=Manager();

# print(manager1.__dict__);

class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, first, last, staffnum):
        Person.__init__(self,first, last)
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber

x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")

print(x.Name())
print(y.GetEmployee())