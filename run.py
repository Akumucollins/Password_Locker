import random
from password_locker import User
from password_locker import Credentials
 
def main():
    while True: 
        print("***Bienvenue to Password Locker!!!***")
        print('\n')
        print("Do you have an account with Password Locker?y/n")
        print("Select the  short code to navigate through:'ex' to log out")
        option = input().lower()
        print('\n')
        
        if option == "y":
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
            
            while confirm_password != created_user_password:
                print("Invalid!!! Password did not match")
                print("Please enter your password again")
                created_user_password = input()
                print("Confirm your password")
                
            else:
                print(f"Congratulations {created_user_name} your have successfully created a Password Locker account")
                print("Select a short code to navigate through:'lg' to login ")
                short_code = input().lower()
                print('\n')
                
                if short_code == 'lg':
                    print("***Proceed to login***")
                    print("Enter account name")
                    entered_accname = input()
                    print("Enter username")
                    entered_username = input()
                    print("Enter password")
                    entered_password = input()
                else:
                   print(f"Welcome {entered_username} to your Password Locker account")
                   print('\n')
                   
               
        
if __name__ == '__main__':
    main()        