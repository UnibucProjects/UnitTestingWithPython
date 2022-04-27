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

    def test_branch_coverage(self):
        with self.assertRaises(Exception) as context:
            coprime_apparitions('', 'A', 2)
            self.assertEqual(context.exception.args[0], Exception('Empty string or string length too big').args[0])

        with self.assertRaises(Exception) as context:
            coprime_apparitions('merge', 'A', 0)
            self.assertEqual(context.exception.args[0], Exception('Invalid number').args[0])

        with self.assertRaises(Exception) as context:
            coprime_apparitions('merge', 'A', 1)
            self.assertEqual(context.exception.args[0], Exception('Invalid character').args[0])

        with self.assertRaises(Exception) as context:
            coprime_apparitions('merge', 'a', 1)
            self.assertEqual(context.exception.args[0], Exception('Empty string or string length too big').args[0])

        self.assertEqual(coprime_apparitions('merge', 'e', 2), False)
        self.assertEqual(coprime_apparitions('merge', 'e', 3), True)

    def test_statement_coverage(self):
        with self.assertRaises(Exception) as context:
            coprime_apparitions("", 'a', 3)
        self.assertEqual(context.exception.args[0], 'Empty string or string length too big')

        with self.assertRaises(Exception) as context:
            coprime_apparitions("abc", 'a', 0)
        self.assertEqual(context.exception.args[0], 'Invalid number')

        with self.assertRaises(Exception) as context:
            coprime_apparitions("abc", 'A', 2)
        self.assertEqual(context.exception.args[0], 'Invalid character')

        with self.assertRaises(Exception) as context:
            coprime_apparitions("a", 'f', 5)
        self.assertEqual(context.exception.args[0], '0 apparitions')

        self.assertFalse(coprime_apparitions("aab", 'a', 4))

        self.assertTrue(coprime_apparitions("aaaab", 'a', 3))

    def test_valid_cases(self):
        self.assertEqual(coprime_apparitions('test', 't', 4), False)
        self.assertEqual(coprime_apparitions('test', 't', 3), True)
        self.assertEqual(coprime_apparitions('tmtmtmtmt', 't', 3), True)


if __name__ == '__main__':
    unittest.main()
