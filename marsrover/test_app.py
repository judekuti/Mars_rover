import unittest
from app import app


class TestApp(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     print('setupClass')

    # @classmethod
    # def tearDownClass(cls):
    #     print('teardownClass')

    # def setUp(self):
    #     print('setUp')
    #     self.date = date
    #     self.url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=' + self.date + '&api_key=G5y2M6Nxqx8ZO7E3Fr4sHOOzWTxmknVNYvOMJnZW'

    # def tearDown(self):
    #     print('tearDown\n')
    # Ensure that app was correctly set-up
    # By testing the response status logged in

    def test_index(self):
        print('Test Index Page')
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that index page loads correctly
    # By testing some content on the page

    def test_index_content(self):
        print('Test Index Page Content')
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'SELECT A DATE TO VIEW PHOTOS OF MARS' in response.data)


if __name__ == '__main__':
    unittest.main()
