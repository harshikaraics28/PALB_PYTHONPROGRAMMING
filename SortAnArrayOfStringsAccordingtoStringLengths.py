class Solution:
    def sortByLength(self, arr):
        # Python's sort is stable, so equal-length strings
        # will keep their original relative order
        arr.sort(key=len)
        return arr
