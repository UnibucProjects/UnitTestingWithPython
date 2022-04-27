import unittest
from main import coprime_apparitions

class MyTestCase(unittest.TestCase):
    def test_conditional_coverage(self):
        with self.assertRaises(Exception) as context:
            coprime_apparitions('abcdefghijklmnoprabcdefghijklmnoprabcdefghijklmnopr', 't', 2)
            self.assertEqual(context.exception.args[0], Exception('Empty string or string length too big').args[0])

        with self.assertRaises(Exception) as context:
            coprime_apparitions('test', 't', -2)
            self.assertEqual(context.exception.args[0], Exception('Invalid number').args[0])

        with self.assertRaises(Exception) as context:
            coprime_apparitions('test', '1', 2)
            self.assertEqual(context.exception.args[0], Exception('Invalid character').args[0])

        with self.assertRaises(Exception) as context:
            coprime_apparitions('test', 'm', 2)
            self.assertEqual(context.exception.args[0], Exception('0 apparitions').args[0])

        with self.assertRaises(Exception) as context:
            coprime_apparitions('', 'm', 2)
            self.assertEqual(context.exception.args[0], Exception('Empty string or string length too big').args[0])

        self.assertEqual(coprime_apparitions('test', 't', 4), False)
        self.assertEqual(coprime_apparitions('test', 't', 3), True)
        self.assertEqual(coprime_apparitions('tmtmtmtmt', 't', 3), True)



if __name__ == '__main__':
    unittest.main()
