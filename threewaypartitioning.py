class Solution:
    # Function to partition the array around the range such 
    # that array is divided into three parts.
    def threeWayPartition(self, arr, a, b):
        
        low = 0
        mid = 0
        high = len(arr) - 1
        
        while mid <= high:
            
            # Case 1: Element < a
            if arr[mid] < a:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            
            # Case 2: Element > b
            elif arr[mid] > b:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
            
            # Case 3: Element in range [a, b]
            else:
                mid += 1
        
        return True
