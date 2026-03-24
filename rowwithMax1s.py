class Solution:
    def rowWithMax1s(self, arr):
        
        n = len(arr)
        m = len(arr[0])
        
        row = 0
        col = m - 1
        
        max_row_index = -1
        
        while row < n and col >= 0:
            
            if arr[row][col] == 1:
                max_row_index = row
                col -= 1   # move left
            else:
                row += 1   # move down
        
        return max_row_index
