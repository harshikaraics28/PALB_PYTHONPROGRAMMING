class Solution:
    def spirallyTraverse(self, mat):
        
        result = []
        
        if not mat:
            return result
        
        n = len(mat)
        m = len(mat[0])
        
        top, bottom = 0, n - 1
        left, right = 0, m - 1
        
        while top <= bottom and left <= right:
            
            # 1. Traverse left → right
            for i in range(left, right + 1):
                result.append(mat[top][i])
            top += 1
            
            # 2. Traverse top → bottom
            for i in range(top, bottom + 1):
                result.append(mat[i][right])
            right -= 1
            
            # 3. Traverse right → left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(mat[bottom][i])
                bottom -= 1
            
            # 4. Traverse bottom → top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(mat[i][left])
                left += 1
        
        return result
