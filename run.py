from password_locker import User
from password_locker import Credentials
 
def create_signup(first_name, last_name, created_user_name, created_user_password, confirm_password):
    """
    Function to create a first time signup
    """
    new_user = User(first_name, last_name, created_user_name, created_user_password, confirm_password)
    return new_user

def save_user(user):
    """
    Function to save user signup details
    """
    user.save_user() 

def add_credentials(default_accname, default_username, default_password):
    """
    Function to add a new account and its credentials
    """
    new_credentials = Credentials(default_accname, default_username, default_password)
    return new_credentials
 
def save_credential(account):
    """
    Function to save account credentials details
    """
    account.save_credentials() 

def display_credentials():
    """
    Function to display  credentials_list
    """
    return Credentials.display_credentials()

def find_credentials(default_accname):
    '''
    Function that finds credentials by account name
    '''

    return Credentials.find_by_name(default_accname)

def existing_credentials(default_accname):
    '''
    Functiion that checks if an account really exists
    '''
    return Credentials.credentials_exists(default_accname)

def delete_credentials(credentials):
    """
    Function to delete an account
    """
    return Credentials.delete_credentials(credentials)

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
            
            save_user(create_signup( first_name, last_name, created_user_name, created_user_password, confirm_password))
            print('-' * 10)
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

                        save_credential(add_credentials(default_accname, default_username, default_password))
                        print('-' * 10)
                        print(f"Welcome {default_username} to your Password Locker account \n Account Name: {default_accname} \n Password: {default_password}")
                        print('\n')    
                        
                    while True:
                        print("Use these short codes : cc - create new credentials, dc - display credentials, de - delete credentials, fc -find credentials, cls -copy credentials , lo - logout the account") 
                        short_code = input().lower()
                    
                        if short_code == 'cc':
                                print("Enter account name")
                                default_accname = input()
                                print("Enter username")
                                default_username = input()
                                print("Enter password")
                                default_password = input()

                                save_credential(add_credentials(default_accname, default_username, default_password))
                                print('-' * 10)
                                print(f"Your Password Locker Application saved a new credentials information as: \n Username: {default_username}  \n Account Name: {default_accname} \n Password: {default_password}")
                                print('\n')
                        
                        elif short_code == 'dc':
                                if display_credentials():
                                    print("Welcome to the list of all your credentials")
                                    print('\n')
                                    
                                    print('-' * 10)
                                    for credential in display_credentials():
                                         print(f" Account Name: {credential.default_accname}  \n Username: {credential.default_username} \n Password: {credential.default_password}")
                                 
                                    print('\n')
                                else:
                                    print('\n')
                                    print(f"You don't seem to have any credentials saved yet")
                                    print('\n')
                                    
                        elif short_code == 'de':
                                print("Enter name of the account you want to delete its credentials")

                                default_accname = input()
                                if existing_credentials(default_accname):
                                    print('\n')
                                    search_account = find_credentials(default_accname)
                                    delete_credentials(search_account)
                                    
                                    print('-' * 10)
                                    print(f"Your Password Locker {default_accname} account deleted successfully")
                                    print('\n')
                                else:
                                    print("The {default_accname} account credentials you want to delete doesn't exist")   
                                    print('\n')
                        elif short_code == 'fc':
                                print("Enter the account name you want to search for")
                                
                                    
                                print('-' * 10)
                                default_accname = input()
                                if existing_credentials(default_accname):
                                    print('\n')
                                    search_account = find_credentials(default_accname)
                                    print(f"Hello, {default_username} your account credentials is as follows:")
                                    
                                    print(f"Account Name: {default_accname}")
                                    print(f"Your Password: {default_password}")
                                    
                                else:
                                    print("The {default_accname} account credentials doesn't exist")
                                    print('\n')
                                    
                        elif  short_code == 'lo':            
                                    print("Goodbye {default_username}  Your have succefully logout your Password Locker account") 
                                    break  
                        else:
                            print("Sorry, invalid short code. Enter a valid code to continue")
                                                     
        elif option == "y":    
               print("*** Login to your Password Locker account ***")
               print("Select a short code to navigate through:lg - login to an account :lo - logout an account")
               short_code = input().lower()
               
               if short_code == 'lo':
                    print("Goodbye....Your have succefully logout your Password Locker account") 
                    break
               
               elif short_code == 'lg':
                    print("*** Login ***")
                    print("Enter account name")
                    default_accname = input()
                    print("Enter username")
                    default_username = input()
                    print("Enter password")
                    
                    default_password = input()
                    save_credential(add_credentials(default_accname, default_username, default_password))
                    print('-' * 10)
                    print(f"Welcome {default_username} to your Password Locker account \n Account Name: {default_accname} \n Password: {default_password}")
                    print('\n')    
                        
                    while True:
                        print("Use these short codes : cc - create new credentials, dc - display credentials, de - delete credentials, fc -find credentials, cls -copy credentials , lo - logout the account") 
                        short_code = input().lower()
                    
                        if short_code == 'cc':
                                print("Enter account name")
                                default_accname = input()
                                print("Enter username")
                                default_username = input()
                                print("Enter password")
                                default_password = input()

                                save_credential(add_credentials(default_accname, default_username, default_password))
                                print('-' * 10)
                                print(f"Your Password Locker Application saved a new credentials information as: \n Username: {default_username}  \n Account Name: {default_accname} \n Password: {default_password}")
                                print('\n')
                        
                        elif short_code == 'dc':
                                if display_credentials():
                                    print("Welcome to the list of all your credentials")
                                    print('\n')
                                    
                                    print('-' * 10)
                                    for credential in display_credentials():
                                         print(f" Account Name: {credential.default_accname}  \n Username: {credential.default_username} \n Password: {credential.default_password}")
                                 
                                    print('\n')
                                else:
                                    print('\n')
                                    print(f"You don't seem to have any credentials saved yet")
                                    print('\n')
                                    
                        elif short_code == 'de':
                                print("Enter name of the account you want to delete its credentials")

                                default_accname = input()
                                if existing_credentials(default_accname):
                                    print('\n')
                                    search_account = find_credentials(default_accname)
                                    delete_credentials(search_account)
                                    print('-' * 10)
                                    print(f"Your Password Locker {default_accname} account deleted successfully")
                                    print('\n')
                                else:
                                    print("The {default_accname} account credentials you want to delete doesn't exist")   
                                    print('\n')
                        elif short_code == 'fc':
                                print("Enter the account name you want to search for")
                                
                                default_accname = input()
                                if existing_credentials(default_accname):
                                    print('\n')
                                    print('-' * 10)
                                    search_account = find_credentials(default_accname)
                                    print(f"Hello, {default_username} your account credentials is as follows:")
                                    
                                    print(f"Account Name: {default_accname}")
                                    print(f"Your Password: {default_password}")
                                    
                                else:
                                    print("The {default_accname} account credentials doesn't exist")
                                    print('\n')
                                    
                        elif  short_code == 'lo':            
                                    print("Goodbye....Your have succefully logout your Password Locker account") 
                                    break  
                        else:
                            print("Sorry, invalid short code. Enter a valid code to continue")
                            
if __name__ == '__main__':
    main()        