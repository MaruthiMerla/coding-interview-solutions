import unittest
from solution import next_number_with_same_bits, next_number_with_same_bits_bitwise

class TestBitwiseMatchingPattern(unittest.TestCase):
    def test_simple_cases(self):
        self.assertEqual(next_number_with_same_bits(6), 9)      # 110 -> 1001
        self.assertEqual(next_number_with_same_bits(12), 17)    # 1100 -> 10001
        self.assertEqual(next_number_with_same_bits(3), 5)      # 11 -> 101
        self.assertEqual(next_number_with_same_bits(8), 16)     # 1000 -> 10000
    
    def test_edge_cases(self):
        self.assertEqual(next_number_with_same_bits(1), 2)      # 1 -> 10
        self.assertEqual(next_number_with_same_bits(0), -1)     # invalid input
        self.assertEqual(next_number_with_same_bits(15), 23)    # 1111 -> 10111
    
    def test_bitwise_version(self):
        self.assertEqual(next_number_with_same_bits_bitwise(6), 9)
        self.assertEqual(next_number_with_same_bits_bitwise(12), 17)
        self.assertEqual(next_number_with_same_bits_bitwise(3), 5)
        self.assertEqual(next_number_with_same_bits_bitwise(8), 16)
        self.assertEqual(next_number_with_same_bits_bitwise(1), 2)
        self.assertEqual(next_number_with_same_bits_bitwise(0), -1)
        self.assertEqual(next_number_with_same_bits_bitwise(15), 23)
    
    def test_large_numbers(self):
        n = 13948  # 11011001111100
        expected = 13967  # 11011010001111
        self.assertEqual(next_number_with_same_bits(n), expected)
        self.assertEqual(next_number_with_same_bits_bitwise(n), expected)

if __name__ == '__main__':
    unittest.main()