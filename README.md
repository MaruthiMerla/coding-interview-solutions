# Sudoku Validator with Custom Zones

This solution validates a 9x9 Sudoku board according to standard Sudoku rules, with the addition of custom zones that must also contain unique digits 1-9.

## Usage

```python
from solution import validate_sudoku

# Example board
board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

# Example custom zone (main diagonal)
custom_zone = [(i, i) for i in range(9)]

# Validate
is_valid = validate_sudoku(board, [custom_zone])
print(is_valid)  # True or False