import unittest
from main import coprime_apparitions


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

    def test_branch_coverage(self):
        with self.assertRaises(Exception) as context:
            coprime_apparitions('', 'A', 2)
            self.assertEqual(context.exception.args[0], 'Empty string or string length too big')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('merge', 'A', 0)
            self.assertEqual(context.exception.args[0], 'Invalid number')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('merge', 'A', 1)
            self.assertEqual(context.exception.args[0], 'Invalid character')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('merge', 'a', 1)
            self.assertEqual(context.exception.args[0], '0 apparitions')

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

    def test_category_partitioning(self):
        with self.assertRaises(Exception) as context:
            coprime_apparitions('_', 'a', 0)
        self.assertEqual(context.exception.args[0], 'Invalid number')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('_', 'a', 1)
        self.assertEqual(context.exception.args[0], 'Invalid number')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('', 'a', 2)
        self.assertEqual(context.exception.args[0], 'Empty string or string length too big')

        self.assertEqual(coprime_apparitions('a', 'a', 2), True)

        with self.assertRaises(Exception) as context:
            coprime_apparitions('a', 'b', 2)
        self.assertEqual(context.exception.args[0], '0 apparitions')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('a', '0', 2)
        self.assertEqual(context.exception.args[0], 'Invalid character')

        self.assertEqual(coprime_apparitions('testing', 't', 2), False)

        with self.assertRaises(Exception) as context:
            coprime_apparitions('wardrobe', 't', 2)
        self.assertEqual(context.exception.args[0], '0 apparitions')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('thestringisok', 'T', 2)
        self.assertEqual(context.exception.args[0], 'Invalid character')

        self.assertEqual(coprime_apparitions('restaurantrestaurantrestaurantrestaurantrestaurant', 'a', 2), False)

        with self.assertRaises(Exception) as context:
            coprime_apparitions('chocolatechocolatechocolatechocolatechocolatechoco', 'x', 2)
        self.assertEqual(context.exception.args[0], '0 apparitions')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('chocolatechocolatechocolatechocolatechocolatechoco', '.', 2)
        self.assertEqual(context.exception.args[0], 'Invalid character')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('chocolatechocolatechocolatechocolatechocolatechocolate', 'p', 2)
        self.assertEqual(context.exception.args[0], 'Empty string or string length too big')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('', 'm', 3)
        self.assertEqual(context.exception.args[0], 'Empty string or string length too big')

        self.assertEqual(coprime_apparitions('s', 's', 3), True)

        with self.assertRaises(Exception) as context:
            coprime_apparitions('x', 'e', 3)
        self.assertEqual(context.exception.args[0], '0 apparitions')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('p', 'W', 3)
        self.assertEqual(context.exception.args[0], 'Invalid character')

        self.assertEqual(coprime_apparitions('madagascar', 'a', 3), True)

        with self.assertRaises(Exception) as context:
            coprime_apparitions('universityofbucharest', 'z', 3)
        self.assertEqual(context.exception.args[0], '0 apparitions')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('informatics', 'A', 3)
        self.assertEqual(context.exception.args[0], 'Invalid character')

        self.assertEqual(coprime_apparitions('subwaysubwaysubwaysubwaysubwaysubwaysubwaysubwaysu', 's', 3), False)

        with self.assertRaises(Exception) as context:
            coprime_apparitions('bucharestbucharestbucharestbucharestbucharestbucha', 'y', 3)
        self.assertEqual(context.exception.args[0], '0 apparitions')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('laptoplaptoplaptoplaptoplaptoplaptoplaptoplaptopla', 'H', 3)
        self.assertEqual(context.exception.args[0], 'Invalid character')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('phonephonephonephonephonephonephonephonephonephonephonephone', 'm', 3)
        self.assertEqual(context.exception.args[0], 'Empty string or string length too big')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('', 'm', 6)
        self.assertEqual(context.exception.args[0], 'Empty string or string length too big')

        self.assertEqual(coprime_apparitions('e', 'e', 8), True)

        with self.assertRaises(Exception) as context:
            coprime_apparitions('b', 'f', 5)
        self.assertEqual(context.exception.args[0], '0 apparitions')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('k', '2', 4)
        self.assertEqual(context.exception.args[0], 'Invalid character')

        self.assertEqual(coprime_apparitions('company', 'm', 9), True)

        with self.assertRaises(Exception) as context:
            coprime_apparitions('printer', 'x', 5)
        self.assertEqual(context.exception.args[0], '0 apparitions')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('faculty', 'Q', 9)
        self.assertEqual(context.exception.args[0], 'Invalid character')

        self.assertEqual(coprime_apparitions('coconutcoconutcoconutcoconutcoconutcoconutcoconutc', 'c', 10), False)

        with self.assertRaises(Exception) as context:
            coprime_apparitions('monkeymonkeymonkeymonkeymonkeymonkeymonkeymonkeymo', 'x', 10)
        self.assertEqual(context.exception.args[0], '0 apparitions')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('chairchairchairchairchairchairchairchairchairchair', ';', 10)
        self.assertEqual(context.exception.args[0], 'Invalid character')

        with self.assertRaises(Exception) as context:
            coprime_apparitions('orangeorangeorangeorangeorangeorangeorangeorangeorange', 'm', 12)
        self.assertEqual(context.exception.args[0], 'Empty string or string length too big')

    def test_valid_cases(self):
        self.assertEqual(coprime_apparitions('test', 't', 4), False)
        self.assertEqual(coprime_apparitions('test', 't', 3), True)
        self.assertEqual(coprime_apparitions('tmtmtmtmt', 't', 3), True)


if __name__ == '__main__':
    unittest.main()
