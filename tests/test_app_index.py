import unittest
import app

class AFirstTestFixture(unittest.TestCase):
    ''' A set of tests that go together is called a fixture, and implemented using a class. '''

    def setUp(self):
        ''' Commands to run before each test in this fixture. This will be run for you automatically by the test framework (unittest/nose/sniffer).  You don't have to use this.  You can if you want/need to. '''
        self.app = app.app.test_client() # Connect this test framework to the app object instantiated in app.py.  This uses Werkzeug's test client (convenient, much?) to do nice things for us.

    def tearDown(self):
        ''' Like setUp, this is run after all tests.  Automatically. '''
        pass

    def test_index_renders_word_gowri_somewhere(self):
        ''' This is a test.  It makes a GET request to a smoketest endpoint (page) from the flask app, and checks to see if the returned value is what we expected.  (Because it should be!) '''
        return_value = self.app.get('/smoketest') # We make a GET request to /smoketest.  This is super easy, because of Werkzeug's test client.
        self.assertEqual(return_value.data, "App appears to be OK, and test fixture is working.") # This assertion is the heart of this test.  Generally, try to have one assertion per test, and probably several tests per fixture (collection of tests)

    def test_something_else(self):
        ''' This is where we'd put another test, and so on as functions in this fixture... '''
        self.assertTrue(True) # It passes!  ...yay.  (Of course)
        # todo: explore what happens if you uncomment the next line:
        # self.assertTrue(False) # Uncomment this out...
        # (the test runner (eg, sniffer) should help you track down what went wrong really quickly)
