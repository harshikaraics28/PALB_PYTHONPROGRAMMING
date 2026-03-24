class Solution:
    def factorial(self, n):
        # Initialize result as 1
        result = [1]
        
        # Multiply numbers from 2 to n
        for num in range(2, n + 1):
            carry = 0
            
            for i in range(len(result)):
                prod = result[i] * num + carry
                result[i] = prod % 10
                carry = prod // 10
            
            # Handle remaining carry
            while carry:
                result.append(carry % 10)
                carry //= 10
        
        # Reverse to get correct order
        result.reverse()
        return result
