from TreeNode import TreeNode
from BST import BST

class BinarySearchTree(BST):
    """
    A binary search tree.
    
    Attributes:
        root: The root of the binary search tree.
    """
    def __init__(self):
        """
        Initializes a binary search tree.
        """
        self._root = None
        
    @property
    def root(self):
        """
        Getter method to provide access to the root attribute.

        Returns:
            The root of the binary search
        """
        return self._root
    
    @root.setter
    def root(self, node):
        """
        Setter method to allow setting the root attribute.

        Args:
            node: The new root of the binary search tree.
        """
        self._root = node

    def insert(self, key, value=None):
        """
        Inserts a key-value pair into the binary search tree.
        If the key already exists in the tree, the associated value is updated.

        Args:
            key: The key to be inserted into the tree.
            value: The value associated with the key, optional
        """
        if self._root is None:
            self._root = TreeNode(key, value)
            return
        
        node = self._root
        
        while node is not None:
            if key < node.key:
                if node.left is None:
                    node.left = TreeNode(key, value)
                    return
                node = node.left
            elif key > node.key:
                if node.right is None:
                    node.right = TreeNode(key, value)
                    return
                node = node.right
            else:
                node.value = value
                return
                
    def search(self, key):
        """
        Searches for a key in the binary search tree and returns the node.
        Raises KeyError if the key is not found.

        Args:
            key: The key to search for in the tree.

        Returns:
            The node associated with the key.

        Raises:
            KeyError: If the key is not found in the tree.
        """
        node = self._root
        
        while node is not None:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node
            
        raise KeyError
    
    def get_value(self, key):
        """
        Searches for a key in the binary search tree and returns the value associated with it.
        Raises KeyError if the key is not found.

        Args:
            key: The key to search for in the tree.

        Returns:
            The value associated with the key.
        """
        return self.search(key).value
    
    def delete(self, key):
        """
        Deletes a key from the binary search tree.

        Args:
            key: The key of the node to be deleted.
        """
        self._root = self._delete_recursive(self._root, key)
    
    def _delete_recursive(self, node, key):
        """
        Recursive helper method for deletion.

        Args:
            node: The current node being checked.
            key: The key to be deleted.

        Returns:
            The node to be deleted.
        """
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            successor = self._find_min(node.right)
            node.key = successor.key
            node.value = successor.value
            node.right = self._delete_recursive(node.right, successor.key)
        
        return node
    
    def _find_min(self, node):
        """
        Find the node with the minimum key in a subtree.

        Args:
            node: The root of the subtree.
        
        Returns:
            The node with the minimum key.
        """
        current = node
        while current.left is not None:
            current = current.left
        return current

    def __len__(self):
        """
        Returns the number of nodes in the tree.

        Returns:
            The number of nodes in the tree.
        """
        return 0 if self._root is None else len(self._root)