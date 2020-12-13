学习笔记
前序遍历:根左右，[root.val] + pre(root.left) + pre(root.right)
中序遍历:左根右，in(root.left) + [root.val] + in(root.right)
后序遍历:左右根，post(root.left) + post(root.right) + [root.val]


对于二叉树和N叉树的层序遍历，或是二叉树和N叉树的最大深度，都可以用同一种解法（BFS）：
1. 首先将root加入到空列表中（queue），定义一个空列表以储存结果（res），用while循环判断停止条件（queue是否为空），并定义一个用于存每一层元素的值（level）。
2. 使用for循环，定义一个当前值（cur)，cur = queue.pop(0) 也就是queue中第一个元素
3. 如果cur的值有效，将cur的值加入level中，并把cur的左右根（二叉树），或是children（N叉树）加入queue中。
4. for循环结束时，把level中的值添加进res中
若是求层序，则返回res， 若是求最大深度，则返回len(res)

代码：
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = [root]
        res = []
        while queue:
            level = []
            for i in range(len(queue)):
                cur = queue.pop(0)
                print(cur)
                if cur:
                    level.append(cur.val)
                    queue.extend([cur.left, cur.right])
            if level:
                res.append(level)
        return res

求深度（DFS）解法：
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        maxLeft = self.maxDepth(root.left)
        maxRight = self.maxDepth(root.right)
        return max(maxLeft, maxRight) + 1