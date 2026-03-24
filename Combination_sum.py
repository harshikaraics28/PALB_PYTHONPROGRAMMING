class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(start, current, remaining):
            # If target becomes 0 → valid combination
            if remaining == 0:
                result.append(list(current))
                return
            
            # If target becomes negative → stop
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                # Choose the candidate
                current.append(candidates[i])
                
                # Reuse same element → pass i (not i+1)
                backtrack(i, current, remaining - candidates[i])
                
                # Backtrack (remove last element)
                current.pop()

        backtrack(0, [], target)
        return result
