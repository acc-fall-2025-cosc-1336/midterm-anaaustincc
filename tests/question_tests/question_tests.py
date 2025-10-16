#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config, get_sum_of_evens

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

