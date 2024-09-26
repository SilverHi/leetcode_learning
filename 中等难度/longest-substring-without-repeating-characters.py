
#对于题目中的描述，首先判断什么是一个无重复子串，即一个字符串中不出现重复字符，并且这个字符串在给定的这个s中。
#所以可以得到第一个直观的思路，从第一位开始遍历，找到最长的不重复子串，然后将第一位给截去 将剩下的当作新的s 继续查找。深搜的思路


class Solution:

    def getLongSubStr(self, s: str, max: int) -> int:
        length = len(s)

        # 判断最长子串
        new_s = []
        for c in s:
            if c not in new_s:
                new_s.append(c)
                continue
            else:
                break
        # print(f"最长：{len(new_s)}")
        if len(new_s) >= max: max = len(new_s)
        if max >= length:
            return max
        else:
            return self.getLongSubStr(s[1:], max)

    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.getLongSubStr(s, 0)
