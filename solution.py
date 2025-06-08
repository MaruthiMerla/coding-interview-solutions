class SudokuValidator:
    def __init__(self, board, custom_zones=None):
        
        self.board = board
        self.custom_zones = custom_zones or []
    
    def is_valid(self):
    
        return (self._check_rows() and 
                self._check_columns() and 
                self._check_boxes() and 
                self._check_custom_zones())
    
    def _check_rows(self):
       
        for row in self.board:
            if not self._is_valid_unit(row):
                return False
        return True
    
    def _check_columns(self):
      
        for col in zip(*self.board):
            if not self._is_valid_unit(col):
                return False
        return True
    
    def _check_boxes(self):
       
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                box = [self.board[x][y] for x in range(i, i+3) 
                                       for y in range(j, j+3)]
                if not self._is_valid_unit(box):
                    return False
        return True
    
    def _check_custom_zones(self):
        
        for zone in self.custom_zones:
            cells = [self.board[r][c] for (r, c) in zone]
            if not self._is_valid_unit(cells):
                return False
        return True
    
    def _is_valid_unit(self, unit):
        
        seen = set()
        for num in unit:
            if num == 0:
                continue  # Skip empty cells
            if num < 1 or num > 9 or num in seen:
                return False
            seen.add(num)
        return True


def validate_sudoku(board, custom_zones=None):
    
    validator = SudokuValidator(board, custom_zones)
    return validator.is_valid()