class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
                # set for tracking prevValues val : index
                prevMap = {}
                # enumerate nums using i(index) and n(value)
                for i, n in enumerate(nums):

                # track the difference between the target and current value
                    diff = target - n
                # if the difference is in set for previous values return prevMap[diff], and index of current value
                    if(diff in prevMap):
                        return [prevMap[diff],i]
                # if the difference is not in the set add the current number to the set with a value of the current index
                    prevMap[n] = i
            