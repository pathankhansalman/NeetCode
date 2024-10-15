class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for num in nums:
            if num not in count_dict:
                count_dict[num] = 0
            count_dict[num] += 1
        return [x[0] for x in sorted([(k, v) for k, v in count_dict.items()], key = lambda x: x[1])][-1*k:]