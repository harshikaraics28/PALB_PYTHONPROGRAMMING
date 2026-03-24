class Solution:
    def countPairs(self, arr):
        n = len(arr)
        count = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                diff = 0
                
                # Compare both strings character by character
                for k in range(len(arr[i])):
                    if arr[i][k] != arr[j][k]:
                        diff += 1
                        if diff > 1:  # Stop early if more than 1 difference
                            break
                
                if diff == 1:
                    count += 1
        
        return count
