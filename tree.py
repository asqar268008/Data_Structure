class TreeNode:
    def __init__(self, data):
        self.data = data
        self.child = []

class Tree:
    def __init__(self):
        self.root = None
    
    def add_child(self, child_data, parent_data=None):
        newChild = TreeNode(child_data)
        if not self.root:
            self.root = newChild
            return
        parenentNode  = self._find_node(self.root, parent_data)
        if parenentNode:
            parenentNode.child.append(newChild)
        else:
            print(f"Parent node with data {parent_data} not found.")
        
    def _find_node(self, node, data):
        if node.data == data:
            return node
        for child in node.child:
            foundNode = self._find_node(child, data)
            if foundNode:
                return foundNode
        return
    
    def delete_node(self, data):
        if not self.root:
            print("Tree is empty.")
            return
        if self.root.data == data:
            self.root = None
            return
        parentNode = self._find_parent(self.root, data)
        if parentNode:
            parentNode.child = [child for child in parentNode.child if child.data != data]
        else:
            print(f"Node with data {data} not found.")

    def _find_parent(self, node, data):
        for child in node.child:
            if child.data == data:
                return node
            parentNode = self._find_parent(child, data)
            if parentNode:
                return parentNode
        return
    
    def PrintTree(self, depth=10, node=None):
        if not node:
            node = self.root
        print(" "*depth, node.data)
        for child in node.child:
            self.PrintTree(depth+2, child)

tree = Tree()
tree.add_child(1)  
tree.add_child(2, 1)
tree.add_child(3, 1)
tree.add_child(4, 2)
tree.add_child(5, 2)
tree.add_child(6, 3)
tree.add_child(7, 3)
tree.add_child(8, 4)
tree.add_child(9, 4)
tree.add_child(10, 5)
tree.add_child(11, 5)
tree.add_child(12, 6)
tree.add_child(13, 6)
tree.add_child(14, 7)
tree.add_child(15, 7)
tree.add_child(16, 8)
tree.add_child(17, 8)
tree.add_child(18, 9)
tree.add_child(19, 9)
tree.PrintTree()
print("After Delection")
tree.delete_node(3)
tree.PrintTree()      