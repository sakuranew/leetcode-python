class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st=0
        p_dic={}
        max_len=0
        for i,c in enumerate(s):
            if c not in p_dic or p_dic[c]<st:
                p_dic[c]=i
            elif p_dic[c]>=st:
                st=p_dic[c]+1
                p_dic[c]=i
            max_len=max(max_len,i-st+1)
        return max_len
