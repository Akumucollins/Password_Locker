import pyperclip
import string
import random

class User:
    
    """
      Class that generates new instances of user.
    """
    
    user_list = []

    def __init__(self,first_name,last_name,user_name,password,confirm_password):
        
      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name 
        self.password = password
        self.confirm_password = confirm_password
        
    def save_user(self):
        
      '''
        Save_user method saves user objects into user_list
      '''
        
      User.user_list.append(self)
        

class Credentials:
    
    """
      Class that generates new instances of credentials.
    """
    
    credentials_list = []

    def __init__(self,default_accname,default_username,default_password):
      
        # docstring removed for simplicity
      
        self.default_accname = default_accname
        self.default_username = default_username
        self.default_password = default_password 
  
    def save_credentials(self):
        
      '''
        Save_credentials method saves credential objects into credentials_list.
      '''

      Credentials.credentials_list.append(self)   
        
    @classmethod
    def display_credentials(cls):
        
      '''
        Method that returns the credentials list.
      '''
      
      return cls.credentials_list
  
    @classmethod
    def find_by_name(cls,acc_name):
        '''
        Method that takes in account name and return credential object that matches that account name
         Args:
              account name:accountname to search for
        return:
               credential of user that matches the account name      
        '''

        for credentials in cls.credentials_list:
            if credentials.account_name == acc_name:
             return credentials
    
    def delete_credentials(self):
        '''
        Delete_credentials method deletes a saved account credentials from the credential_list
        '''
        Credentials.credentials_list.remove(self)
        
    @classmethod 
    def credentials_exists(cls,acc_name):
        '''
        Method that checks if credentials exists from the credentials list.
        Args:
            number: Account name to search if it exists
        Returns :
            Boolean: True or false depending if the credentials exists
        '''
        for credentials in cls.credentials_list:
            if credentials.account_name == acc_name:
             return True

        return False
    
    # @classmethod    
    # def rand_pass(cls, size):  
        
    #     '''
    #     Method that generates a  password for the credentials_list
    #     '''
    #     generate_pass = ''.join([random.choice(  
    #                     string.ascii_lowercase + string.digits)  
    #                     for n in range(size)])  
                            
    #     return generate_pass 
    
       