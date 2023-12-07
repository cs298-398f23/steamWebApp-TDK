from games_app import create_app, get_redis
from werkzeug.security import generate_password_hash
import unittest

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        # Create an instance of the app using the application factory
        app = create_app()

        # Configure the app for testing
        app.config['TESTING'] = True

        # Create a test client using the Flask application configured for testing
        self.app = app.test_client()

        # Set up a test Redis connection (if necessary)
        self.redis = get_redis()

    def test_index_without_login(self):
        result = self.app.get('/')

        self.assertEqual(result.status_code, 302)
        self.assertIn('/login', result.headers['Location'])

    def test_index_with_login(self):
        # Set up a test user
        with self.app as client:
            with client.session_transaction() as sess:
                sess['username'] = 'testuser'

            # While user is in sessino, we can test the index page
            result = client.get('/')
            self.assertEqual(result.status_code, 200)


    def test_login_page_content(self):
        result = self.app.get('/login')

        self.assertIn(b'Login', result.data)
        self.assertIn(b'Username', result.data)
        self.assertIn(b'Password', result.data)

    def test_login(self):
        result = self.app.get('/login')

        self.assertEqual(result.status_code, 200)

    def test_register(self):
        result = self.app.get('/register')

        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Register', result.data)
        self.assertIn(b'Username', result.data)
        self.assertIn(b'Password', result.data)

    def test_logout_without_login(self):
        result = self.app.get('/logout')

        self.assertEqual(result.status_code, 302)
        self.assertIn('/login', result.headers['Location'])

    def test_logout_with_login(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['username'] = 'testuser'

            # Now, make a GET request to the logout route
            response = client.get('/logout', follow_redirects=True)

            # Check if the session has been cleared
            with client.session_transaction() as sess:
                self.assertNotIn('username', sess)

            # Check if the response redirected to the login page
            self.assertEqual(response.status_code, 200)
            self.assertIn('Login', response.data.decode())

    def test_favorites_without_login(self):
        result = self.app.get('/favorites')

        self.assertEqual(result.status_code, 302)
        self.assertIn('/login', result.headers['Location'])

    def test_favorites_with_login(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['username'] = 'testuser'

            # While user is in session, we can test the favorites page
            result = client.get('/favorites')
            self.assertEqual(result.status_code, 200)

    #def test_add_favorite_with_login(self):
        #with self.app as client:
            #with client.session_transaction() as sess:
                #sess['username'] = 'testuser'

            # While user is in session, we can test the favorites page
            #result = client.get('/add_favorite')
            #self.assertEqual(result.status_code, 200)

    #def test_add_favorite_without_login(self):

        #result = self.app.get('/add_favorite')

        #self.assertEqual(result.status_code, 302)
        #self.assertIn('/login', result.headers['Location'])

if __name__ == '__main__':
    unittest.main()


