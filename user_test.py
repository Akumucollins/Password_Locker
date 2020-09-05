import unittest
from password_locker import User

class TestUser(unittest.TestCase):   
     
    def setUp(self):
        
        '''
        Set up method to run before each test cases.
        '''
        
        self.new_user = User("Collins", "Akumu", "akumu_collins", "4321") # create user object
        
    def test_init(self):

        '''
        Test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Collins")
        self.assertEqual(self.new_user.last_name,"Akumu")
        self.assertEqual(self.new_user.user_name,"akumu_collins")
        self.assertEqual(self.new_user.password,"4321")
        
    def test_save_user(self):
      
        '''
        Test_save_credentials test case to test if the contact object is saved into the contact list
        '''
      
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
        
if __name__ == '__main__':
    unittest.main()