import unittest
from main import coprime_apparitions


class MyTestCase(unittest.TestCase):
    def test_equivalence_partitioning_and_boundary_analysis(self):
        with self.assertRaises(Exception) as context:
            coprime_apparitions('', 'a', 2)
        self.assertEqual(context.exception.args[0], 'Empty string or string length too big')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'a', 2)
        self.assertEqual(context.exception.args[0], 'Empty string or string length too big')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('a', 'a', 1)
        self.assertEqual(context.exception.args[0], 'Invalid number')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb', 'a', 1)
        self.assertEqual(context.exception.args[0], 'Invalid number')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('a', 'a', 0)
        self.assertEqual(context.exception.args[0], 'Invalid number')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb', 'a', 0)
        self.assertEqual(context.exception.args[0], 'Invalid number')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('a', 'F', 2)
        self.assertEqual(context.exception.args[0], 'Invalid character')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb', 'F', 2)
        self.assertEqual(context.exception.args[0], 'Invalid character')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('a', 'v', 2)
        self.assertEqual(context.exception.args[0], '0 apparitions')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb', 'v', 2)
        self.assertEqual(context.exception.args[0], '0 apparitions')

        self.assertEqual(coprime_apparitions('a', 'a', 2), True)
        self.assertEqual(coprime_apparitions('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb', 'b', 5), False)
        self.assertEqual(coprime_apparitions('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb', 'b', 11), True)

if __name__ == '__main__':
    unittest.main()
