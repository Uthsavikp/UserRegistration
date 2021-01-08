''' 
  @Author: Uthsavi KP
  @Date: 2021-01-08 23:27:24
  @Last Modified by:  Uthsavi KP
  @Last Modified time: 2021-01-09 01:12:54
  @Title: User Registration Problem 
'''

import re
class UserRegistration:
    def __init__(self):
        """
        cointains all regular expression patterns
        and validating user input using these patterns
        """
        self.name = "^[A-Z][a-zA-Z]{2,}$"
        self.email = "^[a-zA-z]{3}[0-9a-zA-Z\\.\\_\\-\\+]*@[a-z0-9]*\\.(co|com.au|in|net|in|com.com|com|)$"

    def get_user_registration(self):
        """
        contains all the methods 
        """
        user_register.get_first_name() 
        user_register.get_last_name()
        user_register.get_email_address()

    def get_first_name(self):    
        """
        getting input for first name and
        checking if first name starts with 
        capital and has minimum 3 characters
        """
        try:
            first_name_input = input("Enter your first name :")
            if re.match(self.name, first_name_input):
                print("Valid first name")
            else:
                print("Invalid first name,Re enter your name with capital and with minimum 3 characters ")	
                self.get_first_name()
        except Exception as err:
            print(err)    

    def get_last_name(self):
        """
        getting input for last name and
        checking if last name starts with 
        capital and has minimum 3 characters
        """
        try:
            last_name_input = input("Enter your last name :")
            if re.match(self.name, last_name_input):
                print("Valid last name")
            else:
                print("Invalid last name,Re enter your name with capital and with minimum 3 characters ")	
                self.get_last_name()
        except Exception as err:
            print(err)  

    def get_email_address(self):
        """
        getting input for email address
        """
        try:
            email_input = input("Enter your email address :")
            if re.match(self.email, email_input):
                print("Valid email address")
            else:
                print("Invalid email address")	
                self.get_email_address()
        except Exception as err:
            print(err)                  

if __name__ == "__main__":
    user_register = UserRegistration()
    user_register.get_user_registration()
