#Time Complexity:: O(m*n)-all cells in the island matrix has been visited
#Space Complexity:: O(n)-Recursive Stack Space-max length of RS is length of list
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.m = len(grid) #no. of rows
        self.n = len(grid[0]) #no. of columns
        self.count=0 #count to track the number of islands
        self.dirs = [[0,1],[1,0],[-1,0],[0,-1]] #directions array

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j]=="1": #everytime land is detected call dfs
                    self.dfs(grid,i,j)
                    self.count+=1 #increment number of islands

        return self.count

    def dfs(self,grid,i,j):
        #base
        if grid[i][j]=="0": #when no more land is is seen then return
            return
        
        #logic
        grid[i][j]="0" #once land is visited change it to 0 to avoid recursive loop
        for x,y in self.dirs:
            nr = x+i
            nc = y+j
            if nr>=0 and nr<self.m and nc>=0 and nc<self.n: #boundary check
                self.dfs(grid,nr,nc) #recursively call dfs to continue land traversal