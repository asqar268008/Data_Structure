class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def Insertion_at_Begining(self, data):
        newNode = Node(data)
        if self.head is not None:
            self.head.prev = newNode
        self.head.prev = newNode
        newNode.next = self.head
        self.head = newNode

    def Insertion_at_end(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            currNode = self.head
            while currNode.next is not None:
                currNode = currNode.next
            currNode.next = newNode
            newNode.prev = currNode
    
    def Deletion(self, data):
        if self.head is not None:
            if self.head.data == data:
                self.head = self.head.next
                if self.head is not None:
                    self.head.prev = None
            else:
                currNode = self.head
                while currNode is not None:
                    if currNode.data == data:
                        if currNode.next is not None:
                            currNode.next.prev = currNode.prev
                        if currNode.prev is not None:
                            currNode.prev.next = currNode.next
                        return
                    currNode = currNode.next
        else:
            print(f"List is empty, cannot delete {data}")
    
    def length(self):
        count = 0
        if self.head is None:
            return count    
        currNode = self.head
        while currNode is not None:
            count += 1
            currNode = currNode.next
        return count

    def PrintList(self):
        if self.head is None:
            print("List is empty")
            return
        currNode = self.head
        while currNode is not None:
            print(currNode.data,end=" ")
            currNode = currNode.next
        print("\n")

print("Doubly Linkedlist")
linkedlist = DoublyLinkedList()
for i in range(1,12):
    linkedlist.Insertion_at_end(i)
linkedlist.Insertion_at_Begining(0)
linkedlist.PrintList()
print("Length of the LinkedList:",linkedlist.length())
print("After Delection")
linkedlist.Deletion(11)
linkedlist.PrintList()