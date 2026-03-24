class Solution:
    def commonElements(self, arr1, arr2, arr3):
        i = j = k = 0
        n1, n2, n3 = len(arr1), len(arr2), len(arr3)
        
        result = []
        
        while i < n1 and j < n2 and k < n3:
            
            # If all three elements are equal
            if arr1[i] == arr2[j] == arr3[k]:
                
                # Avoid duplicates in result
                if not result or result[-1] != arr1[i]:
                    result.append(arr1[i])
                
                i += 1
                j += 1
                k += 1
            
            # Move pointer of smallest element
            elif arr1[i] < arr2[j]:
                i += 1
            elif arr2[j] < arr3[k]:
                j += 1
            else:
                k += 1
        
        return result if result else [-1]
