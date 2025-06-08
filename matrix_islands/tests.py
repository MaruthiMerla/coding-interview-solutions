import unittest
from solution import count_islands

class TestMatrixIslands(unittest.TestCase):
    def test_empty_grid(self):
        self.assertEqual(count_islands([]), 0)
        self.assertEqual(count_islands([[]]), 0)
    
    def test_single_island(self):
        grid = [
            ['1', '1', '1'],
            ['1', '1', '1'],
            ['1', '1', '1']
        ]
        self.assertEqual(count_islands(grid), 1)
    
    def test_multiple_islands(self):
        grid = [
            ['1', '0', '1'],
            ['0', '1', '0'],
            ['1', '0', '1']
        ]
        self.assertEqual(count_islands(grid), 5)
    
    def test_diagonal_connection(self):
        grid = [
            ['1', '0', '1'],
            ['0', '1', '0'],
            ['1', '0', '1']
        ]
        self.assertEqual(count_islands(grid), 5)
        
        grid = [
            ['1', '0', '1'],
            ['0', '1', '0'],
            ['0', '0', '1']
        ]
        self.assertEqual(count_islands(grid), 3)
    
    def test_sample_case(self):
        grid = [
            ['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']
        ]
        self.assertEqual(count_islands(grid), 3)

if __name__ == '__main__':
    unittest.main()