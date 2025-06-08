import unittest
from solution import shortest_path_with_teleport

class TestKnightsAndPortals(unittest.TestCase):
    def test_simple_grid(self):
        grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(shortest_path_with_teleport(grid), 2)
    
    def test_blocked_path(self):
        grid = [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0]
        ]
        self.assertEqual(shortest_path_with_teleport(grid), 4)
    
    def test_teleport_required(self):
        grid = [
            [0, 1, 1],
            [1, 1, 1],
            [1, 1, 0]
        ]
        self.assertEqual(shortest_path_with_teleport(grid), 2)
    
    def test_no_path(self):
        grid = [
            [0, 1],
            [1, 1]
        ]
        self.assertEqual(shortest_path_with_teleport(grid), -1)
    
    def test_large_grid(self):
        grid = [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]
        ]
        self.assertEqual(shortest_path_with_teleport(grid), 4)
    
    def test_teleport_not_needed(self):
        grid = [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(shortest_path_with_teleport(grid), 4)

if __name__ == '__main__':
    unittest.main()