class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = {}
        def dp(i,j) :
            if (i,j) in m:
                return m[(i,j)]

            if j == len(p):
                return i == len(s)

            first_match = i < len(s) and p[j] in {s[i], '.'}
            if j + 1 <len(p) and p[j+1] == '*':

                res = dp(i,j+2) or (first_match and dp(i+1,j))
            else:
                res = first_match and dp(i+1,j+1)
            
            m[(i,j)] = res
            return res
        return dp(0,0)










