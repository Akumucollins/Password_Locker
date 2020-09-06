from password_locker import User
from password_locker import Credentials
 
def create_signup(first_name,last_name,confirm_password):
    """
    Function to create a first time signup
    """
    new_user = User(first_name,last_name,confirm_password)
    return new_user

def save_user(user):
    """
    Function to save user signup details
    """
    user.save_user() 

def add_credentials(default_accname,default_username,default_password):
    """
    Function to add a new account and its credentials
    """
    new_credentials = Credentials(default_accname,default_username,default_password)
    return new_credentials
 
def save_credential(account):
    """
    Function to save accountcredential details
    """
    account.save_credentials() 
 
def main():
    
    while True: 
        print("*** Welcome to Password Locker!!! ***")
        print('\n')
        print("Do you have an account with Password Locker? y/n")
        option = input().lower()
        
        if option == "n":
            print("Signup to Password Locker account")
            print('Enter first name')
            first_name = input()
            print('Enter last name')
            last_name = input()
            print('Create username')
            created_user_name = input()
            print('Create password')
            created_user_password = input()
            print('Confirm password')
            confirm_password = input()
            
            save_user(create_signup( first_name, last_name, created_user_name, confirm_password))
            print(f"Congratulations, {first_name} {last_name} your have successfully created a Password Locker account \n Your Username is: {created_user_name} \n Your Password is: {confirm_password}")
            
            while True:
                    print("Select a short code to navigate through:lg - login to an account :lo - logout an account")
                    short_code = input().lower()
                    print('\n')
                    
                    if short_code == 'lo':
                        print("Goodbye {first_name} {last_name} Your have succefully logout your Password Locker account") 
                        break
                    
                    elif short_code == 'lg':
                        print("*** Proceed to login ***")
                        print('\n')
                        print("Enter account name")
                        default_accname = input()
                        print("Enter username")
                        default_username = input()
                        print("Enter password")
                        default_password = input()

                        save_credential(add_credentials(default_accname,default_username,default_password))
                        print(f"Welcome {default_username} to your Password Locker account \n Account Name: {default_accname} \n Password: {default_password}")
                        print('\n')    
                        
                    while True:
                        print("Use these short codes : cc - create new credentials, dc - display credentials, de - delete credentials, fc -find credentials, cls -copy credentials , lo - logout the credentials_list") 
                        short_code = input().lower()
                    
                        if short_code == 'cc':
                                print("Enter account name")
                                default_accname = input()
                                print("Enter username")
                                default_username = input()
                                print("Enter password")
                                default_password = input()

                                save_credential(add_credentials(default_accname,default_username,default_password))
                                print(f"Welcome, {default_username} to your Password Locker account \n Account Name: {default_accname} \n Password: {default_password}")
                                print('\n')
                    
        elif option == "y":    
               print("*** Login to your Password Locker account ***")
               print("Select a short code to navigate through:lg - login to an account :lo - logout an account")
               short_code = input().lower()
               
               if short_code == 'lo':
                    print("Goodbye {default_username}  Your have succefully logout your Password Locker account") 
                    break
               
               elif short_code == 'lg':
                    print("*** Login ***")
                    print("Enter account name")
                    default_accname = input()
                    print("Enter username")
                    default_username = input()
                    print("Enter password")
                    default_password = input()
                    print('\n')
                    print(f"You have login successfully") 
                    print('\n')   
             
if __name__ == '__main__':
    main()        