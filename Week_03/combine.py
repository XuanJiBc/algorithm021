class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # 使用python自带包
        return list(itertools.combinations(range(1, n+1), k))

        # 递归
        if n < k or n < 1:
            return []
        if k == 0:
            return [[]]
        if n == k:
            return [[i for i in range(1, n+1)]]
        ans1 = self.combine(n-1, k-1)
        ans2 = self.combine(n-1, k)
        if ans1:
            for i in ans1:
                i.append(n)
        return ans1+ans2
