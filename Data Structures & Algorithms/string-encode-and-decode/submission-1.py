class Solution:

    def encode(self, strs: List[str]) -> str:
        if(len(strs) > 0):
            result = ""
            for s in strs:
                    result = result + s + ";"
            return result[:-1]
        return "-1 Blank List"
    def decode(self, s: str) -> List[str]:
        if(s == "-1 Blank List"):
            return []
        return s.split(';')