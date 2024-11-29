class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""

        for i in range(len(strs)):
            if i == 0:
                common = strs[i]
            else:
                for j in range (len(common)):
                    if j >= len(strs[i]):
                        common = common[:j]
                        break
                    if common[j] != strs[i][j]:
                        common = common[:j]
                        break
        if common == "":
            return ""
        else:
            return common
