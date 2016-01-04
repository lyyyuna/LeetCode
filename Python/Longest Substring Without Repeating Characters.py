class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        dic = {}
        left_bound = 0
        for i, ch in enumerate(s):
            if ch in dic and dic[ch]>=left_bound:
                left_bound = dic[ch]
            dic[ch] = i+1 
            res = max(res, i+1-left_bound)
        return res

if __name__ == '__main__':
    solu = Solution()

    s = 'abca'
    length = solu.lengthOfLongestSubstring(s)
    print length
    s = 'dvdf'
    length = solu.lengthOfLongestSubstring(s)
    print length