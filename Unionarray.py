#You are given two arrays a[] and b[], return the Union of both the arrays in any order.The Union of two arrays is a collection of all distinct elements present in either of the arrays. If an element appears more than once in one or both arrays, it should be included only once in the result.
class Solution:    
    def findUnion(self, a, b):
        # code here
        
        union_set = set(a)
        
        # Add elements of b
        for element in b:
            union_set.add(element)
        
        # Return as a list
        return list(union_set)
