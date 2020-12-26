class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = ten = tewnty = 0
        for i in bills:
            if i == 5:
                five += 1
            if i == 10:
                if five >= 1:
                    five -= 1
                    ten += 1
                else:
                    return False
            if i == 20:
                if ten >= 1 and five >=1:
                    ten -= 1
                    five -= 1
                    tewnty += 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True

