class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # result = defaultdict(list)

        # travNums = {}

        # count = [1] * len(nums)
        # prevProduct = 1
        # prevValue   = -21 
        # for i in range(len(nums)):
        #     if(prevValue == -21):
        #         prevProduct = 1
        #         prevValue = nums[i]
        #     else:
        #         count[i] = prevProduct * count[i]
        #         prevValue

        # count[ord(c) - ord('a')] += 1
        # result[tuple(count)].append(s)
        # return list(result.values())

        count = [1] * len(nums)
        for i in range(len(nums)):
             for j in range(len(nums)):
                if(i!=j):
                    count[i] *= nums[j]
        return list(tuple(count))
