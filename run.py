from password_locker import User
from password_locker import Credentials
 
def main():
    
    while True: 
        print("***Welcome to Password Locker!!!***")
        print('\n')
        print("Do you have an account with Password Locker?y/n")
        print("Select the  short code to navigate through:'lo' to logout")
        option = input().lower()
        print('\n')
        
        if option == "y":
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
                    print('\n')
                    print("Enter account name")
                    entered_accname = input()
                    print("Enter username")
                    entered_username = input()
                    print("Enter password")
                    entered_password = input()
                else:
                   print(f"Welcome {entered_username} to your Password Locker account")
                   print('\n')
                   
        elif option == "n":    
               print("***Login to your Password Locker account***")
               print('\n')
               print("Enter account name")
               default_accname = input()
               print("Enter username")
               default_user_name = input()
               print("Enter password")
               default_user_password = input()
               print('\n')
               
               while default_user_name != 'testuser' or default_user_password != '1234':
                    print("Wrong username or password.Use the format of 'testuser' in username and '1234' in password ")  
                    print('\n')
                    print("Enter account name")
                    default_accname = input()
                    print("Enter username")
                    default_user_name = input()
                    print("Enter password")
                    default_user_password = input()
                    print('\n')
                    
               else:
                   print("You have login successfully") 
                   print('\n')   
               
        elif short_code == "lo":    
            break
        else:
           print("Enter valid code ti continue")    
             
if __name__ == '__main__':
    main()        