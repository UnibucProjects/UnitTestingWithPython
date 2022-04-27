import unittest
from src.main import coprime_apparitions


class MyTestCase(unittest.TestCase):
    def test_conditional_coverage(self):
        with self.assertRaises(Exception) as context:
            coprime_apparitions('abcdefghijklmnoprabcdefghijklmnoprabcdefghijklmnopr', 't', 2)
        self.assertEqual(context.exception.args[0], 'Empty string or string length too big')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('test', 't', -2)
        self.assertEqual(context.exception.args[0], 'Invalid number')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('test', '1', 2)
        self.assertEqual(context.exception.args[0], 'Invalid character')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('test', 'm', 2)
        self.assertEqual(context.exception.args[0], '0 apparitions')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('', 'm', 2)
        self.assertEqual(context.exception.args[0], 'Empty string or string length too big')

        self.assertEqual(coprime_apparitions('test', 't', 4), False)
        self.assertEqual(coprime_apparitions('test', 't', 3), True)
        self.assertEqual(coprime_apparitions('tmtmtmtmt', 't', 3), True)

    def test_branch_coverage(self):
        with self.assertRaises(Exception) as context:
            coprime_apparitions('', 'A', 2)
        self.assertEqual(context.exception.args[0], 'Empty string or string length too big')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('merge', 'A', 0)
        self.assertEqual(context.exception.args[0], 'Invalid number')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('merge', 'A', 1)
        self.assertEqual(context.exception.args[0], 'Invalid number')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('merge', 'a', 3)
        self.assertEqual(context.exception.args[0], '0 apparitions')

        self.assertEqual(coprime_apparitions('mergemergemergemergemergemergemergemerge', 'e', 8), False)
        self.assertEqual(coprime_apparitions('mergemergemergemergemergemerge', 'e', 5), True)

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


if __name__ == '__main__':
    unittest.main()
