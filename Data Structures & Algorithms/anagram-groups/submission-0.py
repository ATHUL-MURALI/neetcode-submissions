from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for num in strs:
            sorted_num = "".join(sorted(num))
            anagrams[sorted_num].append(num)
        return list(anagrams.values())



            