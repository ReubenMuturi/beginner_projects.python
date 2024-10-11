from collections import deque

# Define the possible movements (up, down, left, right)
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def is_valid_move(grid, x, y, visited):
    rows, cols = len(grid), len(grid[0])
    return 0 <= x < rows and 0 <= y < cols and grid[x][y] == 0 and (x, y) not in visited


def bfs(grid, start, end):
    rows, cols = len(grid), len(grid[0])

    # BFS uses a queue to explore cells level by level
    queue = deque([start])
    visited = set()
    visited.add(start)

    # Dictionary to track the path (how we reached each node)
    parent = {start: None}

    while queue:
        current = queue.popleft()

        # If we reached the destination
        if current == end:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]  # Return the path in the correct order

        # Explore all neighbors (up, down, left, right)
        for direction in DIRECTIONS:
            next_x, next_y = current[0] + direction[0], current[1] + direction[1]

            if is_valid_move(grid, next_x, next_y, visited):
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))
                parent[(next_x, next_y)] = current

    # If no path is found, return None
    return None


# Example grid (0 = free, 1 = obstacle)
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)  # Start at top-left corner
end = (4, 4)  # End at bottom-right corner

# Run the pathfinder
path = bfs(grid, start, end)

if path:
    print("Path found:", path)
else:
    print("No path found.")