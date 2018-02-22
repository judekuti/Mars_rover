import unittest
from app import app


class TestApp(unittest.TestCase):
    # Ensure that app was correctly set-up
    # By testing the response status logged in
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that index page loads correctly
    # By testing some content on the page
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'SELECT A DATE TO VIEW PHOTOS OF MARS' in response.data)

    # Ensure date selection behaves correctly
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'SELECT A DATE TO VIEW PHOTOS OF MARS' in response.data)

    # Ensure date selection behaves correctly
    # def setUp(self):
    #     app.config['TESTING'] = True
    #     self.app = app.test_client()

    # def tearDown(self):
    #     print('tearDown\n')

    # def test_marsrover(self):
    #     print('test_marsrover')
    #     with patch('app.requests.get') as app_get:
    #         app_get.return_value.ok = True
    #         app.get.return_value.text = 'Success'

    # response = self.test_client.post(
    #     request_path,
    #     data=data,
    #     follow_redirects=False
    # )
    # expectedPath = '/'
    # self.assertEqual(response.status_code, 302)
    # self.assertEqual(urlparse(response.location).path, expectedPath)

    # def test_monthly_schedule(self):
    #     with patch('employee.requests.get') as mocked_get:
    #         mocked_get.return_value.ok = True
    #         mocked_get.return_value.text = 'Success'

    #         schedule = self.emp_1.monthly_schedule('May')
    #         mocked_get.assert_called_with('http://company.com/Schafer/May')
    #         self.assertEqual(schedule, 'Success')

    #         mocked_get.return_value.ok = False

    #         schedule = self.emp_2.monthly_schedule('June')
    #         mocked_get.assert_called_with('http://company.com/Smith/June')
    #         self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
