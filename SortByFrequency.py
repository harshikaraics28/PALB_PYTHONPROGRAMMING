class Solution:
    def frequencySort(self, s):
        from collections import Counter
        
        # Count frequency of each character
        freq = Counter(s)
        
        # Sort characters:
        # 1. By frequency (ascending)
        # 2. By lexicographical order if frequency is same
        sorted_chars = sorted(freq.items(), key=lambda x: (x[1], x[0]))
        
        # Build result string
        result = ""
        for char, count in sorted_chars:
            result += char * count
        
        return result
