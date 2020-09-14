import unittest
from password_locker import Credentials

class TestUser(unittest.TestCase):   
     
    def setUp(self):
            
        '''
        Set up method to run before each test cases.
        '''
        
        self.new_credentials = Credentials( "twitter", "akumu_collins", "1234")# create credential object
        
    def test_init(self):
        
        '''
        Test_init test case to test if the object is initialized properly
        '''
        
        self.assertEqual(self.new_credentials.default_accname,"twitter")
        self.assertEqual(self.new_credentials.default_username,"akumu_collins")
        self.assertEqual(self.new_credentials.default_password,"1234")

    def test_save_credentials(self):
        
        '''
        Test_save_credentials test case to test if the credential object is saved into the credential list
        '''
        
        self.new_credentials.save_credentials() 
        self.assertEqual(len(Credentials.credentials_list),1)
     
    def tearDown(self):
        '''
        TearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []   
     
    def test_save_multiple_credentials(self):
        
        '''
        Test_save_multiple_credentials to check if we can save multiple credential objects to our credential_list
        ''' 
           
        self.new_credentials.save_credentials() 
        
        test_credentials = Credentials("twitter", "akumu_collins", "1234") # new credential
        test_credentials.save_credentials()
        
        self.assertEqual(len(Credentials.credentials_list),2)
      
    def test_display_all_credentials(self):
        
        '''
        Method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)
        
    def test_find_credentials_by_name(self):
        
        '''
        test to check if we can find a user or credential by account name and display information
        '''
        
        self.new_credentials.save_credentials()
        test_credentials = Credentials("twitter", "akumu_collins", "1234") # new credential
        
        test_credentials.save_credentials()
        found_credentials = Credentials.find_by_name("twitter")
        
        self.assertEqual(found_credentials.user_name,test_credentials.user_name)
        
    def test_delete_credentials(self):
        
        """
        Test to delete account credentials
        """
        
        self.new_credentials.save_credentials()
        
        test_credentials = Credentials("twitter", "akumu_collins", "1234")# new credential
        test_credentials.save_credentials()
        
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
     
    def test_credentials_exists(self):
        '''
        Test to check if we can return a Boolean  if we cannot find the credential.
        '''

        self.new_credentials.save_credentials()
        
        test_credentials = Credentials("twitter", "akumu_collins", "1234")# new credential
        test_credentials.save_credentials()

        credentials_exists = Credentials.credentials_exists("twitter")

        self.assertTrue(credentials_exists)   
    
  
if __name__ == '__main__':
    unittest.main()