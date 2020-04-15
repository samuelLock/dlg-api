import app
import unittest

class Test_sum_up(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(app.sum_up([1,2,10]),13)

    def test_negative_numbers(self):
        self.assertEqual(app.sum_up([-1,-2,10]),7)

    def test_empty_list(self):
        self.assertEqual(app.sum_up([]),0)

    def test_total_is_integer(self):
        self.assertIsInstance(app.sum_up([1,2,10]),int)
    
    def test_total_can_be_float(self):
        self.assertIsInstance(app.sum_up([1,2,10.5]),float)

    def test_strings_cannot_be_used(self):
        with self.assertRaises(TypeError):
            app.sum_up([1,2,"ten"])

if __name__ == '__main__':
    unittest.main()