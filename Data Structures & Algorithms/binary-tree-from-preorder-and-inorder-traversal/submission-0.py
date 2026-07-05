# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # If no nodes are left, return None
        if not preorder or not inorder:
            return None

        # First element of preorder is always the root
        root = TreeNode(preorder[0])

        # Find root position in inorder
        mid = inorder.index(preorder[0])

        # Left subtree
        root.left = self.buildTree(
            preorder[1 : mid + 1],
            inorder[:mid]
        )

        # Right subtree
        root.right = self.buildTree(
            preorder[mid + 1 :],
            inorder[mid + 1 :]
        )

        return root