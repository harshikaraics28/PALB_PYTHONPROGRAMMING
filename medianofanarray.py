class Solution:
    def findMedian(self, arr):
        # Step 1: Sort the array
        arr.sort()
        
        n = len(arr)
        
        # Step 2: Check even or odd length
        if n % 2 == 1:
            return arr[n // 2]
        else:
            return (arr[n // 2 - 1] + arr[n // 2]) / 2
