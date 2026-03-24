class Solution:
    def smallestSubWithSum(self, x, arr):
        
        n = len(arr)
        min_len = float('inf')
        curr_sum = 0
        start = 0
        
        for end in range(n):
            
            # Expand window
            curr_sum += arr[end]
            
            # Shrink window while sum > x
            while curr_sum > x:
                min_len = min(min_len, end - start + 1)
                curr_sum -= arr[start]
                start += 1
        
        return min_len if min_len != float('inf') else 0
