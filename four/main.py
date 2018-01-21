from manager import Manager;
from developer import Developer;

emp1=Developer("ravi","kumar","guru",5000,"python");
emp2=Developer("sunil","Kumar","Raghav",20000,"C++");
mang1=Manager("Me","Check","Out",100000);

mang1.add_employees(emp1);
mang1.add_employees(emp2);
mang1.list_employees();
print("**********************************After Removing employee***************************");
mang1.remove_employees(emp2);
mang1.list_employees();

