def read_maze(filename: str) -> list[list[str]]:
    maze = []
    with open(filename, 'r') as f:
        for i in f:
            line = i.strip()
            row = list(line)
            maze.append(row)
    return maze

def find_start_and_target(maze: list[list[str]]) -> tuple[int, int]:
    S = None
    T = None
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                S = (i , j)
            elif maze[i][j] == 'T':
                T = (i, j)
    return (S, T)



def get_neighbors(maze: list[list[str]], position: tuple[int, int]) -> list[tuple[int, int]]:
    r, c = position
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    neighbors = []

    for row, column in directions:
        potr, potc = r + row, c + column
        if (potr >= 0 and potr < len(maze)) and (potc >= 0 and potc < len(maze[0])) and maze[potr][potc] != "#":
            neighbors.append((potr, potc))
    
    return neighbors

from collections import deque
def bfs(maze: list[list[str]], start: tuple[int, int], target: tuple[int, int]) -> list[tuple[int, int]]:
    queue = deque([(start,[start])])
    visited = {start}
    while queue:
        current_node, path = queue.popleft()

        if current_node == target:
            return path
        
        for neighbor in get_neighbors(maze, current_node):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))
    return None



def dfs(maze: list[list[str]], start: tuple[int, int], target: tuple[int, int]) -> list[tuple[int, int]]:
    stack = [(start, [start])]
    visited = {start}

    while stack:
        current_node, path = stack.pop()

        if current_node == target:
            return path
        
        for neighbor in reversed(get_neighbors(maze, current_node)):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                stack.append((neighbor, new_path))
    return None



def print_maze_with_path(maze: list[list[str]], path: list[tuple[int, int]]) -> None:
    RED = "\033[91m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    RESET = "\033[0m"

    for r, c in path: 
        if maze[r][c] not in ('S', 'T'):
            maze[r][c] = '*'

    for row in maze:
        for ch in row:
            if ch == 'S':
                print(YELLOW + ch + RESET, end = '')
            elif ch == 'T':
                print(GREEN + ch + RESET, end = '')
            elif ch == '*':
                print(RED + ch + RESET, end = '')
            else:
                print(ch, end = '')
        print()

import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Incorrect arguments entered: py search_maze.py dfs/bfs mazex.txt required")
        sys.exit(1)
    alg_chosen = sys.argv[1]
    filename = sys.argv[2]
    maze = read_maze(filename)

    start, target = find_start_and_target(maze)

    if alg_chosen == "bfs":
        path = bfs(maze, start, target)
    elif alg_chosen == "dfs":
        path = dfs(maze, start, target)
    
    print_maze_with_path(maze, path)