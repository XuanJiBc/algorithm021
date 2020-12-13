class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dit = {}
        for i in s:
            if i not in dit:
                dit[i] = 1 
            else:
                dit[i] += 1
        for j in t:
            if j not in dit:
                return False
            else:
                if dit[j] == 0:
                    return False
                dit[j] -= 1
        for i in dit:
            if dit[i] != 0:
                return False
        return True