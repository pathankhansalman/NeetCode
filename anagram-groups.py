class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_sorted = [''.join(list(sorted(list(strin)))) for strin in strs]
        strs_dict = {}
        for i, strin in enumerate(strs_sorted):
            if strin in strs_dict:
                strs_dict[strin].append(i)
            else:
                strs_dict[strin] = [i]
        return [[strs[i] for i in v] for _, v in strs_dict.items()]