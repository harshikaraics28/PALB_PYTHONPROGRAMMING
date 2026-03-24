class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        
        # Traverse from last digit
        for i in range(n - 1, -1, -1):
            
            # If digit is less than 9, just add 1
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # If digit is 9, make it 0 (carry over)
            digits[i] = 0
        
        # If all digits were 9 (e.g., 999 → 1000)
        return [1] + digits
