from TreeNode import TreeNode
from TreePrinter import print_tree

class MinHeap:
    """This class implements a linked binary min-heap.

    The heap will support insertion, extraction of the minimum element,
    and dynamic deletion of nodes by reference. The heap is a binary tree
    with nodes of type TreeNode.

    Attributes:
        root: Optional[TreeNode] the root node of the heap. If the heap
            is empty, this is None.
    """
    def __init__(self):
        """Creates a new, empty heap"""
        self.root: TreeNode = None

        # We use a protected attribute to store the current size
        # of the heap. This keeps us from needing to recompute the size.
        # Any delete or insert operations must update this protected
        # attribute to ensure the size remains correct!
        self._size = 0

    def __len__(self):
        """Return the number of nodes stored in the heap.

        Returns:
            int: the number of nodes in the heap.
        """
        return self._size

    def _swap_node_with_parent(self, x: TreeNode):
        """Swaps the given node with its parent in the heap.
       
        This method will actually swap the TreeNodes for a node
        and its parent, rather than simply swapping the values. As part
        of the swap, all links to parents and children will be altered
        so that afterwards the given node assumes the role of its parent
        and vice-versa in the linked tree structure. This means that
        all references to the node x should still refer to x after the swap.

        Args:
             x: a TreeNode object that should be swapped with its parent.
        
        Raises:
             ValueError: if x does not have a parent.
        """
        p = x.parent
        if p is None:
            raise ValueError("Node {x} has no parent")

        # Save the left and right children of p and x then break these
        # links from p to its children (including x)
        pr, pl = p.right, p.left
        p.right, p.left = None, None

        # Now we put x into the correct position with respect to p's
        # parent p2:
        p2 = p.parent
        # If p was the root, make x the root instead
        if p2 is None:
            self.root = x
        # If p was a left child of its parent, make x the left child
        # of this parent instead
        elif p2.left is p:
            p2.left = x
        # If p was a right child of its parent, make x a right child
        # instead
        else:
            p2.right = x

        # Next we need to exchange x and p's children One of these
        # will be x so we need to put that in the position that p was
        # in:

        # First, save x's old left and right children, then break
        # these links
        xl, xr = x.left, x.right
        x.left, x.right = None, None
        # Next, set x's new children to be p's old children, except...
        # ...if x was a left child of p, then p should be a left 
        # child of x
        if x is pl:
            x.left = p
            x.right = pr
        # ...if x was a right child of p, then p should be a right
        # child of x
        else:
            x.left = pl
            x.right = p
        # Finally, make p's new children x's old children
        p.left = xl
        p.right = xr


    def _replace_node_with_leaf(self, node: TreeNode, leaf: TreeNode):
        """Replaces the given node with the given leaf node.
       
        This method will first remove the leaf node from the linked
        structure. It will then rearrange the linked structure so that 
        the given leaf node takes the role of node: all of node's children
        will be made children of the leaf node, and node's parent will
        become the parent of the leaf node. After the operation, node will
        have no parent or children.

        Args:
             node: a TreeNode object that is the node we wish to replace.
             leaf: a TreeNode object that is a leaf node that we will
                 replace node with. This node should not have any children
                 and should have a parent. That is, it should be a leaf 
                 and also not the root of the heap.

        Returns:
             TreeNode: the node that was replaced. This node will have
                 no children and no parent after the replacement operation.

        Raises:
             ValueError: if leaf has any children or has no parent.
        """
        # Make sure leaf is a leaf and has a parent:
        if (leaf.left is not None) or (leaf.right is not None):
            raise ValueError("The specified node is not a leaf")
        if leaf.parent is None:
            raise ValueError("The specified node has no parent")
        # Remove the leaf node from its parent
        leaf.parent.remove_leaf(leaf)
        # Remove the children from the replaced node, and then assign them
        # as children to the leaf that is replacing node.
        nl, nr = node.left, node.right
        node.left, node.right = None, None
        leaf.left, leaf.right = nl, nr

        # Insert the leaf node into the same position as the removed
        # node:

        # Check if the removed node is the root. If so, we make
        # replacement leaf the root:
        if node.parent is None:
            self.root = leaf
        # Otherwise, make the leaf the left or right child of the replaced
        # node's parent, as appropriate:
        elif node is node.parent.left:
            node.parent.left = leaf
        else:
            node.parent.right = leaf
        return node

    def _get_node_at(self, ix):
        """Returns the node at the given index in the heap.

        Args:
            ix: The index of the node to retrieve (must be positive).

        Returns:
            TreeNode: The node at the given index.

        Raises:
            KeyError: If the index is out of bounds or not positive.
            KeyError: If the node at the given index does not exist.
        """
        if ix <= 0 or ix > self._size:
            raise KeyError(f"Index {ix} out of bounds for heap of size {self._size}")
        
        adjusted_ix = ix - 1
        
        bit_list = [int(bit) for bit in bin(adjusted_ix + 1)[2:]]
        
        current = self.root
        
        for bit in bit_list[1:]:
            if bit == 0:
                current = current.left
            else:
                current = current.right
                
            if current is None:
                raise KeyError(f"Node at index {ix} does not exist in the heap")
                
        return current
            
    def _add_leaf(self, node):
        """
        Adds a new leaf node to the heap.
        
        Args:
            node: The node to add as a leaf.
            
        Raises:
            KeyError: If the index is out of bounds or not positive.
        """
        ix = self._size + 1

        if ix == 1:
            self.root = node
            self._size += 1
            return

        parent_ix = ix // 2

        try:
            parent = self._get_node_at(parent_ix)
        except KeyError:
            raise KeyError(f"Could not find parent at index {parent_ix} while inserting at {ix}. Heap size: {self._size}")

        node.parent = parent
        if ix % 2 == 0:
            parent.left = node
        else:
            parent.right = node

        self._size += 1


    def _sift_up(self, node):
        """Sift up the given node in the heap.
        
        Args:
            node: The node to sift up.
        """
        while node is not None and node.parent is not None and node.key < node.parent.key:
            self._swap_node_with_parent(node)


    def _sift_down(self, node):
        """Sift down the given node in the heap.

        Args:
            node: The node to sift down.
        """
        while True:
            left = node.left
            right = node.right

            if left is None and right is None:
                break

            if left is not None and (right is None or left.key < right.key):
                min_child = left
            elif right is not None:
                min_child = right
            else:
                break

            if node.key <= min_child.key:
                break

            self._swap_node_with_parent(min_child)

    def insert_node(self, node):
        """Inserts a node into the heap.

        Args:
            node: The node to insert.

        Returns:
            TreeNode: The newly inserted node.
        """
        if self.root is None:
            self.root = node
            self._size = 1
            return node

        self._add_leaf(node)
        self._sift_up(node)
        return node

    
    def extract(self):
        """Extracts the minimum element from the heap.

        Returns:
            TreeNode: The minimum element in the heap.

        Raises:
            KeyError: If the heap is empty.
        """
        if self.root is None:
            raise KeyError("Heap is empty")

        min_node = self.root

        if self._size == 1:
            self.root = None
        elif self.root.left is None and self.root.right is None:
            self.root = None
        else:
            last_node = self._get_node_at(self._size)
            self._replace_node_with_leaf(self.root, last_node)
            self._sift_down(self.root)

        self._size -= 1
        return min_node
        
    def delete_node(self, node):
        """ Deletes a node from the heap.
        
        Args:
            node: The node to delete.

        Returns:
            TreeNode: The deleted node.
        
        Raises:
            KeyError: If the heap is empty or if the node is None.
            KeyError: If the node is not found in the heap.
        
        """
        if node is None or self.root is None:
            raise KeyError("Cannot delete from empty heap or delete None node")

        if self._size == 1:
            if node is self.root:
                self.root = None
                self._size = 0
                return node
            raise KeyError("Node not found in heap")

        last_node = self._get_node_at(self._size)
        self._size -= 1

        if node is last_node:
            parent = last_node.parent
            if parent.left is last_node:
                parent.left = None
            else:
                parent.right = None
            last_node.parent = None
            return node

        is_child = (node.left is last_node) or (node.right is last_node)

        self._replace_node_with_leaf(node, last_node)

        if last_node.left:
            last_node.left.parent = last_node
        if last_node.right:
            last_node.right.parent = last_node

        if is_child:
            if last_node.left is last_node:
                last_node.left = None
            if last_node.right is last_node:
                last_node.right = None

        if last_node.parent and last_node.key < last_node.parent.key:
            self._sift_up(last_node)
        else:
            self._sift_down(last_node)

        return node
    

    def insert(self, key, value=None):
        """Inserts a new node with the given key and value into the heap.

        Args:
            key: The key of the new node.
            value: The value of the new node (optional).

        Returns:
            TreeNode: The newly inserted node.
        """
        new_node = TreeNode(key, value)
        return self.insert_node(new_node)