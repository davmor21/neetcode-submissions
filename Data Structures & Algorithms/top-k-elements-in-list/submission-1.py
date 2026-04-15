class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Initialize set for counting frequency of each number
        # Initialize array of empty arrays for the range of the length of nums + 1 (1 for each possible frequency)
        # for each number in nums add 1 to the set for counting frequency of numbers
        # for each number, count in count append the number at the index of the count to the array of counts]
        # initialize empty array for result
        # loop through frequency array from highest to lowest, appending the int's to the result array
            # return the result if the length of the result = k 
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n, c in count.items():
            freq[c].append(n)
        
        result = []

        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result