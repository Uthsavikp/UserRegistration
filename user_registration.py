''' 
  @Author: Uthsavi KP
  @Date: 2021-01-08 23:27:24
  @Last Modified by:  Uthsavi KP
  @Last Modified time: 2021-01-08 23:27:24
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

if __name__ == "__main__":
    user_register = UserRegistration()
    user_register.get_first_name()        