class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def Insertion_at_Begining(self, data):
        newNode = Node(data)
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
    
    def Deletion(self, data):
        if self.head is not None:
            if self.head.data == data:
                self.head = self.head.next
            else:
                currNode = self.head
                while currNode.next is not None:
                    if currNode.next.data == data:
                        currNode.next = currNode.next.next
                        return
                    currNode = currNode.next
        else:
            print(f"List is empty, cannot delete {data}")

    def search(self, data):
        currNode = self.head
        while currNode is not None:
            if currNode.data == data:
                return True
            currNode = currNode.next
        return False

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

print("Singly Linkedlist")
linkedlist = LinkedList()
for i in range(1,12):
    linkedlist.Insertion_at_end(i)
linkedlist.Insertion_at_Begining(0)
linkedlist.PrintList()
print("Length of the LinkedList:",linkedlist.length())
print("After Delection")
linkedlist.Deletion(11)
linkedlist.PrintList()