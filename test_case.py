import unittest
from solution import Graduation

class TestGraduation(unittest.TestCase):
    def test_valid_input(self):
        graduation_obj = Graduation(5)
        result = graduation_obj.graduation_ceremony()
        self.assertEqual(result, "14/29")  # Expected result for 5 days
        
        graduation_obj = Graduation(4)
        result = graduation_obj.graduation_ceremony()
        self.assertEqual(result, "7/15")  # Expected result for 4 days

        # Add more test cases for different valid inputs

    def test_invalid_input(self):
        graduation_obj = Graduation(0)
        result = graduation_obj.graduation_ceremony()
        self.assertEqual(result, "number of day can not be less than 1 and and it should only integer")

        graduation_obj = Graduation(-3)
        result = graduation_obj.graduation_ceremony()
        self.assertEqual(result, "number of day can not be less than 1 and and it should only integer")

        graduation_obj = Graduation(3.5)
        result = graduation_obj.graduation_ceremony()
        self.assertEqual(result, "number of day can not be less than 1 and and it should only integer")

        # Add more test cases for different invalid inputs

if __name__ == '__main__':
    unittest.main()