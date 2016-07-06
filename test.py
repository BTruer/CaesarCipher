from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the text appears correctly
    def test_indexLoadsProp(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'Input Plaintext:' in response.data)



if __name__ == '__main__':
    unittest.main()
