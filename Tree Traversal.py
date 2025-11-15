class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class TreeTraversal:
    def __init__(self):
        self.root = None
    
    def add(self, data):
        if not self.root:
            self.root = Node(data)
        self._add_recursive(data, self.root)

    def _add_recursive(self,data, node):
        if data < node.data:
            if not node.left:
                node.left = Node(data)
                return
            self._add_recursive(data, node.left)
        elif data > node.data:
            if not node.right:
                node.right = Node(data)
                return
            self._add_recursive(data, node.right)
    
    def Inorder(self):
        result = []
        self._Inorder(self.root, result)
        print("Inorder:",result)
    
    def _Inorder(self,node,result):
        if not node:
            return None
        self._Inorder(node.left, result)
        result.append(node.data)
        self._Inorder(node.right, result)

    def Preorder(self):
        result = []
        self._Preorder(self.root, result)
        print("Preorder:",result)

    def _Preorder(self,node,result):
        if not node:
            return None
        result.append(node.data)
        self._Preorder(node.left, result)
        self._Preorder(node.right, result)

    def Postorder(self):
        result = []
        self._Postorder(self.root, result)
        print("Postorder:",result)

    def _Postorder(self,node,result):
        if not node:
            return None
        self._Postorder(node.left, result)
        self._Postorder(node.right, result)
        result.append(node.data)

    def Levelorder(self):
        queue = [self.root]
        result = []

        while queue:
            node = queue.pop(0)
            result.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        print("Level Order:", result)
        
tree = TreeTraversal()
tree.add(4)
tree.add(1)
tree.add(2)
tree.add(3)
tree.add(5)
tree.add(6)
tree.add(7)
print("Tree Traversal")
print("Breadth First Search(BFS) Traversal")
tree.Inorder()
tree.Preorder()
tree.Postorder()
print("\n")
print("Depth First Search(DFS) Traversal")
tree.Levelorder()