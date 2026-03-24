class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()   # Sort to handle duplicates
        result = []
        
        def backtrack(start, current, remaining):
            if remaining == 0:
                result.append(list(current))
                return
            
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Choose element
                current.append(candidates[i])
                
                # Move to next index (i+1) → use once only
                backtrack(i + 1, current, remaining - candidates[i])
                
                # Backtrack
                current.pop()
        
        backtrack(0, [], target)
        return result
