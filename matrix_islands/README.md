# Matrix Islands with Diagonals

This solution counts the number of islands in a matrix where islands are connected horizontally, vertically, or diagonally.

## Usage

```python
from solution import count_islands

grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]
islands = count_islands(grid)
print(islands)  # 3