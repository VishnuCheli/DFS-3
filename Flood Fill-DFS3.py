#Time Complexity:: O(2^n)-all nodes are visited in the binary tree
#Space Complexity:: O(n)-Recursive Stack Space-max length of RS is length of list
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        self.dirs = [[0,1],[1,0],[-1,0],[0,-1]] #directions array
        self.colorTBC = image[sr][sc] #color to be changed
        self.fillWith = color #color to be filled with
        self.image = image #make the image a global variable 
        self.m = len(image) #no. of rows in image
        self.n = len(image[0]) #no. of columns in images

        if self.colorTBC == color: #if the color to be changed is already the filled color don't continue
            return image

        self.dfs(sr,sc) #dfs function call if image can be filled with different color

        return self.image

    def dfs(self,sr,sc):
        #base - boundary check and check if sr,sc is having color to be changed
        #logic
        self.image[sr][sc] = self.fillWith #change the image pixel color to new color
        for x,y in self.dirs:
            nr = x+sr
            nc = y+sc #check for boundary condition in the image and that new pixel is a color to be changed
            if nr>=0 and nr<self.m and nc>=0 and nc<self.n and self.image[nr][nc]==self.colorTBC:
                self.dfs(nr,nc) #recursively call dfs

        return #return once completed changing all TBC pixels to new color