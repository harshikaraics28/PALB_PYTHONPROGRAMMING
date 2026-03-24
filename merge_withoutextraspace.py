class Solution:
    def mergeArrays(self, a, b):
        n = len(a)
        m = len(b)
        
        gap = (n + m + 1) // 2
        
        while gap > 0:
            i = 0
            j = gap
            
            while j < (n + m):
                
                # Case 1: Both pointers in array a
                if i < n and j < n:
                    if a[i] > a[j]:
                        a[i], a[j] = a[j], a[i]
                
                # Case 2: i in a and j in b
                elif i < n and j >= n:
                    if a[i] > b[j - n]:
                        a[i], b[j - n] = b[j - n], a[i]
                
                # Case 3: Both pointers in b
                else:
                    if b[i - n] > b[j - n]:
                        b[i - n], b[j - n] = b[j - n], b[i - n]
                
                i += 1
                j += 1
            
            if gap == 1:
                gap = 0
            else:
                gap = (gap + 1) // 2
