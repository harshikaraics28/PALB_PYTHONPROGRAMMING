class Solution:
    def minParentheses(self, s):
        open_count = 0   # Unmatched '('
        insertions = 0   # Insertions needed
        
        for char in s:
            if char == '(':
                open_count += 1
            else:  # char == ')'
                if open_count > 0:
                    open_count -= 1
                else:
                    insertions += 1  # Need one '('
        
        # Remaining unmatched '(' need ')'
        return insertions + open_count
