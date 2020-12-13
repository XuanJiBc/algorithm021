# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def dfs(root):
            if root:
                res.append(root.val)
                dfs(root.left)
                dfs(root.right)
        
        res = []
        dfs(root)
        return res

        # 第二种写法
        # if root == None:
        #     return []
        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)