# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(root):
            if root:
                dfs(root.left)
                res.append(root.val)          
                dfs(root.right)

        res = []
        dfs(root)
        return res

        # 第二种方法
        # if root == None:
        #     return []
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)