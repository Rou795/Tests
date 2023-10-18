import unittest
from main import folder_maker

# вытаскиваю токен из файла

with open('token_ya.txt') as f:
    token = f.read()

class API_test(unittest.TestCase):

    def test_folder_creation(self):
        response = folder_maker(token, 'новая папка')
        expected = 201
        self.assertEqual(response, expected)

    def test_zero_token(self):
        response = folder_maker('token', 'новая папка')
        expected = 'не авторизован'
        self.assertEqual(response, expected)
