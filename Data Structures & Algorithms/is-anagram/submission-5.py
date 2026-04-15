class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):                          # Can't be an anagram if not the same length
            return False

        countS, countT = {},{}                                    # initialize sets for counting letters


        for i in range(len(s)):                                    # words are both the same length, looping through length
            countS[s[i]] = 1 + countS.get(s[i],0)                  # adding 1 to the count of the character at index i for the string s
            countT[t[i]] = 1 + countT.get(t[i],0)                  # adding 1 to the count of the character at index i for the string t

        for c in countS:                                    # for each character in the countS set
            if(countS[c] != countT.get(c,0)):    # if the count for the character c in the String s doesn't match the count of the character c in the string T
                return False
        return True