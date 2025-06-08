

from collections import deque

def shortest_path_with_teleport(grid):
   
    if not grid or not grid[0]:
        return -1
    
    rows, cols = len(grid), len(grid[0])
    if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
        return -1
    
    directions = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        (1, -2), (1, 2),
        (2, -1), (2, 1)
    ]
    
    no_teleport = bfs(grid, directions, False)
    if no_teleport != -1:
        return no_teleport
    
    return bfs(grid, directions, True)

def bfs(grid, directions, allow_teleport):
    rows, cols = len(grid), len(grid[0])
    visited = [[-1 for _ in range(cols)] for _ in range(rows)]
    queue = deque()
    queue.append((0, 0, False))
    visited[0][0] = 0
    
    empty_cells = []
    if allow_teleport:
        empty_cells = [(i, j) for i in range(rows) 
                       for j in range(cols) if grid[i][j] == 0]
    
    while queue:
        x, y, teleport_used = queue.popleft()
        
        if x == rows - 1 and y == cols - 1:
            return visited[x][y]
        
     
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                if visited[nx][ny] == -1 or visited[nx][ny] > visited[x][y] + 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny, teleport_used))
        
    
        if allow_teleport and not teleport_used:
            for (tx, ty) in empty_cells:
             
                if (tx == x and ty == y) or grid[tx][ty] == 1:
                    continue
                
                if visited[tx][ty] == -1 or visited[tx][ty] > visited[x][y] + 1:
                    visited[tx][ty] = visited[x][y] + 1
                    queue.append((tx, ty, True))
    
    return -1