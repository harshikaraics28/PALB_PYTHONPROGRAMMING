class Solution:
        
    def minSwap(self, arr, k):
        
        n = len(arr)
        
        # Step 1: Count elements <= k
        good = 0
        for num in arr:
            if num <= k:
                good += 1
        
        # Step 2: Count bad elements in first window
        bad = 0
        for i in range(good):
            if arr[i] > k:
                bad += 1
        
        min_swaps = bad
        
        # Step 3: Slide the window
        for i in range(good, n):
            
            # Remove element going out of window
            if arr[i - good] > k:
                bad -= 1
            
            # Add new element coming into window
            if arr[i] > k:
                bad += 1
            
            min_swaps = min(min_swaps, bad)
        
        return min_swaps
