from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        res = []

        for s in strs:
            s_sorted = tuple(sorted(s))
            anagram_map[s_sorted].append(s)
        
        for value in anagram_map.values():
            res.append(value)
        
        return res
