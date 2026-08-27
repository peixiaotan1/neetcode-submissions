class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return "-"
        if strs == [""]: return ""

        res = ""
        for s in strs:
            res += str(len(s))
            res += " "
        res += "#"

        res += "".join(strs)
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        if s == "-": return []
        if s == "": return [""]

        aa = []

        i = 0
        temp = ""
        while i < len(s):
            if s[i] == "#": break

            if s[i] != " ":
                temp += s[i]
            else:
                aa.append(int(temp))
                temp = ""
            i += 1

        res = []
        s = s[i+1: ]
        startindex = 0
        for i in range(len(aa)):
            res.append(s[startindex : aa[i]+startindex])
            startindex += aa[i] 
        return res


