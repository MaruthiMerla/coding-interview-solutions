import unittest
from solution import alien_order

class TestAlienDictionary(unittest.TestCase):
    def test_simple_case(self):
        words = ["wrt", "wrf", "er", "ett", "rftt"]
        self.assertEqual(alien_order(words), "wertf")
    
    def test_empty_input(self):
        self.assertEqual(alien_order([]), "")
    
    def test_single_word(self):
        self.assertEqual(alien_order(["hello"]), "hlo")
        self.assertEqual(alien_order(["a", "a", "a"]), "a")
    
    def test_invalid_order(self):
        words = ["abc", "ab"]
        self.assertEqual(alien_order(words), "")
    
    def test_multiple_possible_orders(self):
        words = ["z", "x", "z"]
        self.assertEqual(alien_order(words), "")
    
    def test_cycle_detection(self):
        words = ["a", "b", "a"]
        self.assertEqual(alien_order(words), "")
    
    def test_sample_case_1(self):
        words = ["wrt", "wrf", "er", "ett", "rftt"]
        self.assertEqual(alien_order(words), "wertf")
    
    def test_sample_case_2(self):
        words = ["z", "x"]
        self.assertEqual(alien_order(words), "zx")
    
    def test_sample_case_3(self):
        words = ["z", "x", "z"]
        self.assertEqual(alien_order(words), "")

if __name__ == '__main__':
    unittest.main()