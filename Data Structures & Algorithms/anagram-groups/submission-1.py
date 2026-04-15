class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #initalize a defaultdict(list) for the base case of the possibility of a blank string
        result = defaultdict(list)
        # for string in strs
        for s in strs:

        # strs[i] is made up of lowercase English letters, so that means there are 26 possibilities
        # initialize a set of 26 0's to track count of each character a-z, a = index 0, z = index 25
            count = [0] * 26
        # loop through each character in the current string
            for c in s:

        # add 1 to the count for the current character's index
                count[ord(c) - ord('a')] += 1
        # append the tracked set to the initial list as the index but as a tuple (to allow to use it as a key) with the string as the value
            result[tuple(count)].append(s)
        # return the final defaultdict as a list
        return list(result.values())