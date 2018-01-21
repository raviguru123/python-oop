from employee import Employee

class Developer(Employee):

    def __init__(self,first_name,middle_name,last_name,pay,prog_language):
        super(Developer,self).__init__(first_name,middle_name,last_name,pay);
        self.prog_language=prog_language;
        
        
