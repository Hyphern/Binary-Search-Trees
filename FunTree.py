from TreeNode import TreeNode
from BinaryTree import inorder, postorder, preorder

tree1 = TreeNode(10)
tree1.left = TreeNode(5)
tree1.right = TreeNode(15)
tree1.left.left = TreeNode(2)
tree1.left.right = TreeNode(8)
tree1.right.left = TreeNode(12)
tree1.right.right = TreeNode(18)

# print("Inorder:")
# inorder(tree1)
# print("Preorder:")
# preorder(tree1)
# print("Postorder:")
# postorder(tree1)
print(tree1.depth)