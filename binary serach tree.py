class BSTNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def add(self, data):
        if not self.root:
            self.root = BSTNode(data)
            return
        self._add_recursive(data, self.root)
    
    def _add_recursive(self, data, node):
        if data < node.data:
            if not node.left:
                node.left = BSTNode(data)
                return
            self._add_recursive(data, node.left)

        elif data > node.data:
            if not node.right:
                node.right = BSTNode(data)
                return
            self._add_recursive(data, node.right)
    
    def remove(self, data):
        if not self.root:
            print("Tree is empty")
            return 
        if self.root.data == data:
            self.root = None
            return
        self._remove_recursive(data, self.root)
    
    def _remove_recursive(self, data, node):
        if node.left and node.left.data == data:
            node.left = None
            return
        elif node.right and node.right.data == data:
            node.right = None
            return
        elif data < node.data:
            self._remove_recursive(data, node.left)
        elif data > node.data:
            self._remove_recursive(data, node.right)
        
    def display(self):
        result = []
        self._inorder_Traversal(self.root, result)
        print(result)
    
    def _inorder_Traversal(self, node, result):
        if not node:
            return None
        else:
            self._inorder_Traversal(node.left, result)
            result.append(node.data)
            self._inorder_Traversal(node.right, result)
    
    def search(self, data):
        node = self._search_recursive(data,self.root)
        if node:
            print("True")
        else:
            print("False")

    def _search_recursive(self,data, node):
        if node and node.data == data:
            return node
        elif data < node.data:
            return self._search_recursive(data,node.left)
        elif data > node.data:
            return self._search_recursive(data, node.right)

bst = BST()
bst.add(4)
bst.add(1)
bst.add(2)
bst.add(3)
bst.add(5)
bst.add(6)
bst.add(7)
bst.display()
bst.search(4)
print("After Deletion")
bst.remove(7)
bst.display()
bst.remove(3)
bst.display()