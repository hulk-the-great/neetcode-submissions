class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        islands = 0

        def bfs(start_row, start_col):
            queue = deque()
            queue.append((start_row, start_col))
            visited.add((start_row, start_col))

            directions = [
                (1, 0),   # down
                (-1, 0),  # up
                (0, 1),   # right
                (0, -1)   # left
            ]

            while queue:
                row, col = queue.popleft()

                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change

                    if (
                        new_row in range(rows)
                        and new_col in range(cols)
                        and grid[new_row][new_col] == "1"
                        and (new_row, new_col) not in visited
                    ):
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1

        return islands