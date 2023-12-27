import unittest

from Encriptions.Playfair import Playfair


class Playfaier_test(unittest.TestCase):
    def test_one(self):
        res = Playfair('Дядина', 'Зашифрованное сообщение')
        assert res.encrypted_word == "жбюехсйжбаамгткапашёанги"