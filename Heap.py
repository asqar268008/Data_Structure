class HeapNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class MinHeap:
    def __init__(self):
        self.root = None

    def add(self, data):
        if not self.root:
            self.root = HeapNode(data)
            return
        self._add(data, self.root)
    
    def _add(self, data, node):
        if not node.left:
            node.left = HeapNode(data)
            self._heapify_up(node.left)
        elif not node.right:
            node.right = HeapNode(data)
            self._heapify_up(node.right)
        else:
            if self._get_count(node.left) <= self._get_count(node.right):
                self._add(data, node.left)
                return
            self._add(data, node.right)
    
    def _get_count(self,node):
        if not node:
            return 0
        return 1 + self._get_count(node.left) + self._get_count(node.right)
    
    def _heapify_up(self,node):
        while node and node != self.root:
            parentNode = self._get_parentNode(node, self.root)
            if parentNode.data > node.data:
                parentNode.data, node.data = node.data, parentNode.data
                node = parentNode
            else:
                break

    def _get_parentNode(self, node, root):
        if root.left == node or root.right == node:
            return root
        if root.left:
            parent = self._get_parentNode(node,root.left)
            if parent:
                return parent
        if root.right:
            parent = self._get_parentNode(node,root.right)
            if parent:
                return parent
        return None
    
    def extract(self):
        if not self.root:
            print("Heap is empty")
            return
        min = self.root.data
        last_node = self._remove()
        if last_node:
            self.root.data = last_node
            self._heapify_down(self.root)
        else:
            self.root = None
        return min
    
    def _remove(self):
        queue = [self.root]
        last_node = None
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if not node.left and not node.right:
                last_node = node
        if last_node:
            parentNode = self._get_parentNode(last_node, self.root)
            if parentNode.left == last_node:
                parentNode.left = None
            else:
                parentNode.right = None
            return last_node.data
        return None
    
    def _heapify_down(self, node):
        while node:
            min = node
            if node.left and node.left.data < min.data:
                min = node.left
            if node.right and node.right.data < min.data:
                min = node.right
            if min != node:
                min.data, node.data = node.data, min.data
            else:
                break

    def display(self):
        if not self.root:
            print("Heap is empty")
            return
        
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.data, end=" ")
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()

class MaxHeap:
    def __init__(self):
        self.root = None

    def add(self, data):
        if not self.root:
            self.root = HeapNode(data)
            return
        self._add(data, self.root)
    
    def _add(self, data, node):
        if not node.left:
            node.left = HeapNode(data)
            self._heapify_up(node.left)
        elif not node.right:
            node.right = HeapNode(data)
            self._heapify_up(node.right)
        else:
            if self._get_count(node.left) <= self._get_count(node.right):
                self._add(data, node.left)
                return
            self._add(data, node.right)
    
    def _get_count(self,node):
        if not node:
            return 0
        return 1 + self._get_count(node.left) + self._get_count(node.right)
    
    def _heapify_up(self,node):
        while node and node != self.root:
            parentNode = self._get_parentNode(node, self.root)
            if parentNode.data < node.data:
                parentNode.data, node.data = node.data, parentNode.data
                node = parentNode
            else:
                break

    def _get_parentNode(self, node, root):
        if root.left == node or root.right == node:
            return root
        if root.left:
            parent = self._get_parentNode(node,root.left)
            if parent:
                return parent
        if root.right:
            parent = self._get_parentNode(node,root.right)
            if parent:
                return parent
        return None
    
    def extract(self):
        if not self.root:
            print("Heap is empty")
            return
        min = self.root.data
        last_node = self._remove()
        if last_node:
            self.root.data = last_node
            self._heapify_down(self.root)
        else:
            self.root = None
        return min
    
    def _remove(self):
        queue = [self.root]
        last_node = None
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if not node.left and not node.right:
                last_node = node
        if last_node:
            parentNode = self._get_parentNode(last_node, self.root)
            if parentNode.left == last_node:
                parentNode.left = None
            else:
                parentNode.right = None
            return last_node.data
        return None
    
    def _heapify_down(self, node):
        while node:
            max = node
            if node.left and node.left.data > max.data:
                max = node.left
            if node.right and node.right.data > max.data:
                max = node.right
            if max != node:
                max.data, node.data = node.data, max.data
            else:
                break

    def display(self):
        if not self.root:
            print("Heap is empty")
            return
        
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.data, end=" ")
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()

print("Heap Data Structure\n")
print("Min Heap")
minheap = MinHeap()
minheap.add(10)
minheap.add(7)
minheap.add(6)
minheap.add(5)
minheap.add(4)
minheap.add(3)
minheap.display()
print("After Extract")
minheap.extract()
minheap.display()
print("\n")

maxheap = MaxHeap()
maxheap.add(10)
maxheap.add(7)
maxheap.add(6)
maxheap.add(5)
maxheap.add(4)
maxheap.add(3)
maxheap.display()
print("After Extract")
maxheap.extract()
maxheap.display()