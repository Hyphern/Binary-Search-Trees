from Node import Node

class TreeNode(Node):
    """
    A node in a binary tree.
    
    Attributes:
        key: The value stored in the node.
        left: The left child of the node.
        right: The right child of the node.
        parent: The parent of the node.
        value: The value associated
        depth: The depth of the node in the tree.
    """
    def __init__(self, key, value=None):
        """
        Initializes a TreeNode with a key and an optional value.
        
        Args:
            key: The value to be stored in the node.
            value: The value associated with the key, optional.
        """
        self._key = key
        self._left = None
        self._right = None
        self._parent = None
        self._value = value

    @property
    def key(self):
        """
        Getter method to provide access to the key attribute.

        Returns:
            The key of the node.
        """
        return self._key
    
    @key.setter
    def key(self, key):
        """
        Setter method to allow setting the key attribute.

        Args: 
            key: The new key to be associated with the node.
        """
        self._key = key
    
    @property
    def parent(self):
        """
        Getter method to provide access to the parent attribute.
        
        Returns:
            The parent of the node.
        """
        return self._parent

    @parent.setter
    def parent(self, node: 'Node'):
        """
        Setter method to allow setting the parent attribute.
        
        Args:
            node: The new parent of the node.

        Raises:
            TypeError: If the node is not an instance of TreeNode.
        """
        if not (isinstance(node, Node) or node is None):
            raise TypeError
        self._parent = node
    
    @property
    def left(self):
        """
        Getter method to provide access to the left attribute.

        Returns:
            The left child of the node.
        """
        return self._left  

    @left.setter
    def left(self, node: 'Node'):
        """
        Setter method to allow setting the left attribute.
        
        Args:
            node: The new left child of the node.

        Raises:
            TypeError: If the node is not an instance of TreeNode.
        """
        if not (isinstance(node, Node) or node is None):
            raise TypeError("Node must be an instance of TreeNode or None")
                
        if self._left is not None:
            self._left._parent = None
                
        self._left = node

        if node is not None:
            node._parent = self

    @property
    def right(self):
        """
        Getter method to provide access to the right attribute.

        Returns:
            The right child of the node.
        """
        return self._right
    
    @right.setter
    def right(self, node: 'Node'):
        """
        Setter method to allow setting the right attribute.
        
        Args:
            node: The new right child of the node.

        Raises:
            TypeError: If the node is not an instance of TreeNode.
        """
        if not (isinstance(node, Node) or node is None):
            raise TypeError("Node must be an instance of TreeNode or None")
        
        if self.right is not None:
            self._right._parent = None
        
        self._right = node

        if node is not None:
            node._parent = self

    @property
    def value(self):
        """
        Getter method to provide access to the value attribute.

        Returns:
            The value associated with the node.
        """
        return self._value
    
    @value.setter
    def value(self, value):
        """
        Setter method to allow setting the value attribute.
        
        Args:
            value: The new value to be associated with the node.
        """
        self._value = value

    @property
    def depth(self):
        """
        Getter method to provide access to the depth attribute.

        Returns:
            The depth of the node.
        """
        if self.parent is None:
            return 1
        else:
            return self.parent.depth + 1
        
    def __repr__(self):
        """
        Returns a string representation of the node.

        Returns:
            A string representation of the node.
        """
        parent_key = self.parent.key if self.parent is not None else None
        return f"TreeNode(key={self.key}, left={self.left}, right={self.right}, parent={parent_key})"
    
    def remove_leaf(self, node):
        """
        Removes a leaf node from the tree.
        
        Args:
            node: The node to be removed.

        Returns:
            The node that was removed.

        Raises:
            TypeError: If the node is not an instance of TreeNode.
            ValueError: If the node is not a leaf node.    
        """
        if not isinstance(node, TreeNode):
            raise TypeError("Node must be an instance of TreeNode")
        
        if node.left is not None or node._right is not None:
            raise ValueError("Node is not a leaf node")
        
        if self.left is node:
            self.left = None
            return node
        elif self.right is node:
            self.right = None
            return node
        else:
            raise ValueError("Node is not a child of this node")
        
