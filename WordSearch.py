class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])
        
        def dfs(r, c, index):
            # If all characters matched
            if index == len(word):
                return True
            
            # Boundary & mismatch check
            if (r < 0 or c < 0 or 
                r >= rows or c >= cols or 
                board[r][c] != word[index]):
                return False
            
            # Mark as visited
            temp = board[r][c]
            board[r][c] = "#"
            
            # Explore 4 directions
            found = (dfs(r+1, c, index+1) or
                     dfs(r-1, c, index+1) or
                     dfs(r, c+1, index+1) or
                     dfs(r, c-1, index+1))
            
            # Backtrack
            board[r][c] = temp
            
            return found
        
        # Start search from every cell
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        
        return False
