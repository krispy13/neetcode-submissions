class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i, n in enumerate(nums):
            hmap[n] = i

        for i,n in enumerate(nums):
            difference = target - n
            if difference in hmap and hmap[difference] != i:
                return [i, hmap[difference]]
        return []