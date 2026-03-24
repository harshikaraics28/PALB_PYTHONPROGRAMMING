class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        def backtrack(start, current):
            # Add current subset to result
            result.append(list(current))
            
            for i in range(start, len(nums)):
                # Include nums[i]
                current.append(nums[i])
                
                # Move to next index
                backtrack(i + 1, current)
                
                # Backtrack
                current.pop()
        
        backtrack(0, [])
        return result
