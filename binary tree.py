class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def add_node(self, data):
        if not self.root:
            self.root = BinaryTreeNode(data)
            return
        self._add_node_recursive(data, self.root)
    
    def _add_node_recursive(self, data, node):
        if node.left is None:
            node.left = BinaryTreeNode(data)
        elif node.right is None:
            node.right = BinaryTreeNode(data)
        else:
            self._add_node_recursive(data, node.left)
    
    def display(self, depth=0, node=None):
        if node is None:
            node = self.root
        print(" "*depth, node.data)
        if node.left:
            self.display(depth + 2, node.left)
        if node.right:
            self.display(depth + 2, node.right)

    def delete_node(self, data):
        if not self.root:
            print("Tree is empty.")
            return
        if self.root.data == data:
            self.root = None
            return
        self._delete_node_recursive(data, self.root)

    def _delete_node_recursive(self, data, node):
        if node.left and node.left.data == data:
            node.left = None
            return
        if node.right and node.right.data == data:
            node.right = None
            return
        if node.left:
            self._delete_node_recursive(data, node.left)
        if node.right:
            self._delete_node_recursive(data, node.right)
    
    def search(self, data):
        Nodefound = self._search_node_recursive(data, self.root)
        if Nodefound:
            print("True")
        else:
            print("False")

    def _search_node_recursive(self, data, node):
        if not node or node.data == data:
            return node
        return self._search_node_recursive(data, node.left) or self._search_node_recursive(data, node.right)

binarytree = BinaryTree()
binarytree.add_node(5)
binarytree.add_node(1)
binarytree.add_node(2)
binarytree.add_node(3)
binarytree.add_node(4)
binarytree.display()
print("After Delection")
binarytree.delete_node(3)
binarytree.display()
binarytree.search(3)