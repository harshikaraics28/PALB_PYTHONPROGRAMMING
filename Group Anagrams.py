class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_map = {}
        
        for word in strs:
            # Sort the word to create key
            key = "".join(sorted(word))
            
            # Add word to dictionary
            if key not in anagram_map:
                anagram_map[key] = []
            
            anagram_map[key].append(word)
        
        # Return grouped anagrams
        return list(anagram_map.values())
