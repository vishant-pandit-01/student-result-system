class Login:
    def __init__(self):
        self.correct_username="vishant"
        self.correct_password="99535110"
        
    def username(self):
        self.username=input("enter username:-")
        if self.username==self.correct_username:
            return True
        else:
            print("wrong username")
            return False
        
class Success(Login):
    def password(self):
        password=input("enter password:-")
        
        if password==self.correct_password:
            print("login succefully")
        else:
            print("try again")
A2=Success()
if A2.username():
    A2.password()
else:
    print("Login Failed")
