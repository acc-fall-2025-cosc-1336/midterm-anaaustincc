#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config, get_sum_of_evens
from src.question_b.question_b import get_fahrenheit
from src.question_c.question_c import is_prime
from src.question_d.question_d import get_assessment_value, get_tax_assessed

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())


class Test_Question_A(unittest.TestCase):

    def test_get_sum_of_evens_11(self):
        self.assertEqual(30, get_sum_of_evens(11))
    
    def test_get_sum_of_evens_10(self):
        self.assertEqual(30, get_sum_of_evens(10))
    
    def test_get_sum_of_evens_8(self):
        self.assertEqual(20, get_sum_of_evens(8))


class Test_Question_B(unittest.TestCase):

    def test_get_fahrenheit_0(self):
        self.assertEqual(32, get_fahrenheit(0))
    
    def test_get_fahrenheit_5(self):
        self.assertEqual(41, get_fahrenheit(5))
    
    def test_get_fahrenheit_10(self):
        self.assertEqual(50, get_fahrenheit(10))


class Test_Question_C(unittest.TestCase):

    def test_is_prime_4(self):
        self.assertEqual(False, is_prime(4))
    
    def test_is_prime_5(self):
        self.assertEqual(True, is_prime(5))
    
    def test_is_prime_11(self):
        self.assertEqual(True, is_prime(11))

class Test_Question_D(unittest.TestCase):

    def test_get_assessment_value(self):
        self.assertEqual(6000, get_assessment_value(10000))
        self.assertEqual(12000, get_assessment_value(20000))

    def test_get_tax_assessed(self):
        self.assertAlmostEqual(43.2, get_tax_assessed(6000), places=2)
        self.assertAlmostEqual(72.0, get_tax_assessed(10000), places=2)

