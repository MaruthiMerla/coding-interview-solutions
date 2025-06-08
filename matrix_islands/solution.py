

def count_islands(grid):
    
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                count += 1
                dfs(grid, i, j, rows, cols)
    
    return count

def dfs(grid, i, j, rows, cols):
    """Depth-first search to mark all connected land as visited."""
    if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != '1':
        return
    
    grid[i][j] = '0'
    
    directions = [(-1,-1), (-1,0), (-1,1),
                  (0,-1),          (0,1),
                  (1,-1),  (1,0), (1,1)]
    
    for di, dj in directions:
        dfs(grid, i + di, j + dj, rows, cols)