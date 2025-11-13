class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def Insertion_at_Begining(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            newNode.next = newNode
            newNode.prev = newNode
        else:
            tail = self.head.prev
            newNode.next = self.head
            newNode.prev = tail
            tail.next = newNode
            self.head.prev = newNode
            self.head = newNode
    
    def Insertion_at_end(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            newNode.next = newNode
            newNode.prev = newNode
        else:
            tail = self.head.prev
            tail.next = newNode
            newNode.prev = tail
            newNode.next = self.head
            self.head.prev = newNode
    
    def Deletion(self, data):
        if self.head is None:
            print(f"List is empty, cannot delete {data}")
            return
        currNode = self.head
        while True:
            if currNode.data == data:
                if currNode.next == currNode:  # only one node
                    self.head = None
                else:
                    currNode.prev.next = currNode.next
                    currNode.next.prev = currNode.prev
                    if currNode == self.head:
                        self.head = currNode.next
                return
            currNode = currNode.next
            if currNode == self.head:
                break
        
    def length(self):
        count = 0
        if self.head is None:
            return count
        currNode = self.head
        while True:
            count += 1
            currNode = currNode.next
            if currNode == self.head:
                break
        return count
        
    def PrintList(self):
        if self.head is None:
            print("List is empty")
            return
        currNode = self.head
        while True:
            print(currNode.data, end=" ")
            currNode = currNode.next
            if currNode == self.head:
                break
        print("\n")

print("Circulat Linkedlist")
linkedlist = CircularLinkedList()
for i in range(1,12):
    linkedlist.Insertion_at_end(i)
linkedlist.Insertion_at_Begining(0)
linkedlist.PrintList()
print("Length of the LinkedList:",linkedlist.length())
print("After Delection")
linkedlist.Deletion(11)
linkedlist.PrintList()