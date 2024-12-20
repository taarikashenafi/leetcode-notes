# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/

# Clarification:
# - Can the input grid be empty?
# - Do diagonally connected 1s count as part of the same island?
# - Is it acceptable to modify the input grid?
# - Can the input grid contain either only 0s or 1s?


# Approach: Depth-First Search (DFS)
# Time complexity: O(m*n), where m and n are the dimensions of the grid. For brevity, we can declare the time complexity as O(n^2) if the grid is square.
# Space complexity: O(m*n), where m and n are the dimensions of the grid. For brevity, we can declare the space complexity as O(n^2) if the grid is square.

# To solve this problem, we can use a depth-first search (DFS) approach to traverse the grid and identify the islands.
# We start by iterating over each cell in the grid. If the cell is part of an island (marked with '1') and has not been visited, we increment the island count and perform a DFS to mark all connected cells as visited.
# The DFS algorithm works by exploring the neighbors of the current cell (up, down, left, right) until we reach a cell that is not part of the island. We mark each visited cell as '0' to avoid revisiting it. This way, we ensure that each island is counted only once.
# We can start the DFS from any cell on the grid that is part of an island. We then mark all connected cells as visited by recursively calling the DFS function on all of its neighbors.
# Finally, we return the island count.

class Solution(object):
    def numIslands(self, grid):
        if not grid:  # Check if the grid is empty
            return 0  # Return 0 as there are no islands
        
        m, n = len(grid), len(grid[0])  # Get the dimensions of the grid
        count = 0  # Initialize island count
        
        for i in range(m):  # Iterate over each row
            for j in range(n):  # Iterate over each column
                if grid[i][j] == '1':  # Check if the cell is part of an island
                    self.dfs(grid, i, j)  # Perform DFS to mark the island
                    count += 1  # Increment the island count
        return count  # Return the total number of islands

    def dfs(self, grid, row, col): # Implement the depth-first search function
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != '1':
            return  # Return if out of bounds or not part of an island
        grid[row][col] = '0'  # Mark the cell as visited by setting it to '0'
        self.dfs(grid, row + 1, col)  # Visit the cell below
        self.dfs(grid, row - 1, col)  # Visit the cell above
        self.dfs(grid, row, col + 1)  # Visit the cell on the right
        self.dfs(grid, row, col - 1)  # Visit the cell on the left

# Test cases:
solution = Solution()
print(solution.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])) # Output: 1
print(solution.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])) # Output: 3

