import unittest
from solution import Graduation

class TestGraduation(unittest.TestCase):

    def test_valid_input(self):
        graduation_obj = Graduation()

        result = graduation_obj.graduation_ceremony(5)
        self.assertEqual(result, "14/29")  

        result = graduation_obj.graduation_ceremony(10)
        self.assertEqual(result, "372/773")

        result = graduation_obj.graduation_ceremony(4)
        self.assertEqual(result, "7/15")  

        result = graduation_obj.graduation_ceremony(1)
        self.assertEqual(result, "1/2")  

    def test_invalid_input(self):
        graduation_obj = Graduation()
        error_message = "number of days can not be less than 1 or fraction."

        result = graduation_obj.graduation_ceremony(-5)
        self.assertEqual(result, error_message)  

        result = graduation_obj.graduation_ceremony(0)
        self.assertEqual(result, error_message) 

        result = graduation_obj.graduation_ceremony(3.7)
        self.assertEqual(result, error_message)  

        result = graduation_obj.graduation_ceremony("AABD")
        self.assertEqual(result, error_message) 

    def test_large_input(self):
        graduation_obj = Graduation()
        error_message = "number of days can not be less than 1 or fraction."

        result = graduation_obj.graduation_ceremony(100000)
        self.assertNotEqual(result,error_message)

if __name__ == '__main__':
    unittest.main()
#ram_shyam    