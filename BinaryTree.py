from TreeNode import TreeNode

def inorder(node):
    """
    Performs an inorder traversal (left, root, right) and returns the values as a list.
    """
    if node is None:
        return []
    
    result = []
    result.extend(inorder(node.left))
    result.append(node.key)
    result.extend(inorder(node.right))
    
    return result

def preorder(node):
    """
    Performs a preorder traversal (root, left, right) and returns the values as a list.
    """
    if node is None:
        return []
    
    result = [node.key]
    result.extend(preorder(node.left))
    result.extend(preorder(node.right))
    
    return result

def postorder(node):
    """
    Performs a postorder traversal (left, right, root) and returns the values as a list.
    """
    if node is None:
        return []
    
    result = []
    result.extend(postorder(node.left))
    result.extend(postorder(node.right))
    result.append(node.key)
    
    return result