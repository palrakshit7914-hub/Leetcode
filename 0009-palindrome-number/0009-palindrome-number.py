class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num_string = str(x)
        reversed_string = num_string[::-1]

        if num_string == reversed_string:
            return True
        else:
            return False