import unittest
from collections import deque
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        noof_islands=0
        visited=set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.isValid(i,j,grid):
                    if self.getId(i,j) not in visited and grid[i][j]=='1':
                        self.bfs_traversal(i,j,grid,visited)
                        noof_islands+=1
        return noof_islands

    def bfs_traversal(self, i,j,grid,visited):
        q=deque([self.getId(i,j)])
        visited.add(self.getId(i,j))
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        while q:
            current=q.popleft()
            for i,j in directions:
                nRow=self.getRow(current)+i
                nCol=self.getCol(current)+j
                if self.isValid(nRow,nCol,grid):
                    if self.getId(nRow,nCol) not in visited and grid[nRow][nCol]=='1':
                        q.append(self.getId(nRow,nCol))
                        visited.add(self.getId(nRow,nCol))




    def isValid(self,i,j,grid):
        return i>=0 and i<len(grid) and j>=0 and j<len(grid[0])

    def getId(self,i,j):
        return i*1000+j

    def getRow(self,id):
        return id//1000

    def getCol(self,id):
        return id-self.getRow(id)*1000


class NumberOfIslandsTests(unittest.TestCase):
    def test_island_counts(self) -> None:
        test_cases = [
            (
                "Example 1",
                ["11110", "11010", "11000", "00000"],
                1,
            ),
            (
                "Example 2",
                ["11000", "11000", "00100", "00011"],
                3,
            ),
            ("Single water cell", ["0"], 0),
            ("Single land cell", ["1"], 1),
            ("All water", ["000", "000"], 0),
            ("All land", ["111", "111"], 1),
            ("Diagonal contact only", ["10", "01"], 2),
            ("Single row", ["11001101"], 3),
            ("Single column", ["1", "0", "1", "1"], 2),
            ("Land surrounding a hole", ["111", "101", "111"], 1),
            ("Maximum grid, all land", ["1" * 300] * 300, 1),
            (
                "Maximum grid, alternating land and water",
                ["10" * 150, "01" * 150] * 150,
                45_000,
            ),
        ]

        for name, rows, expected in test_cases:
            with self.subTest(name=name):
                grid = [list(row) for row in rows]
                actual = Solution().numIslands(grid)
                status = "PASS" if actual == expected else "FAIL"
                grid_description = " / ".join(rows) if len(rows) * len(rows[0]) <= 40 else (
                    f"{len(rows)} x {len(rows[0])} grid"
                )
                print(f"{status}: {name} ({grid_description}) | expected {expected}, got {actual}",
                      flush=True)
                self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
