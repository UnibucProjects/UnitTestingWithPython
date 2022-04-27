import unittest
from main import coprime_apparitions

class MyTestCase(unittest.TestCase):
    def test_error_cases(self):
        with self.assertRaises(Exception):
            coprime_apparitions('abcdefghijklmnoprabcdefghijklmnoprabcdefghijklmnopr', 't', 2)
        with self.assertRaises(Exception):
            coprime_apparitions('test', 't', -2)
        with self.assertRaises(Exception):
            coprime_apparitions('test', '1', 2)
        with self.assertRaises(Exception):
            coprime_apparitions('test', 'm', 2)
        with self.assertRaises(Exception):
            coprime_apparitions('', 'm', 2)

    def test_valid_cases(self):
        self.assertEqual(coprime_apparitions('test', 't', 4), False)
        self.assertEqual(coprime_apparitions('test', 't', 3), True)
        self.assertEqual(coprime_apparitions('tmtmtmtmt', 't', 3), True)
if __name__ == '__main__':
    unittest.main()
