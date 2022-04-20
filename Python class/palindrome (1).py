# Node class
class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize
        # next as null


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None
        self.length = 0

    # This function prints contents of linked list
    # starting from head
    def printList(self):
        temp = self.head
        while (temp != None):
            print(temp.data)
            temp = temp.next

    def getNthNode(self, n):
        if not n < self.length:
            return
        count = 0
        curr = self.head
        while count < n:
            count += 1
            curr = curr.next
        return curr

    def insert(self, data, index):
        if index > self.length:
            return
        newNode = Node(data)

        if index == 0:
            tmp = self.head
            self.head = newNode
            newNode.next = tmp
            self.length += 1
            return

        prevNode = self.getNthNode(index-1)

        tmp = prevNode.next
        prevNode.next = newNode
        newNode.next = tmp
        self.length += 1

    def deleteIndex(self, index):
        if not index < self.length:
            return
        if index == 0:
            self.head = self.head.next
            return
        prevNode = self.getNthNode(index-1)
        prevNode.next = prevNode.next.next
        self.length -= 1

    def length(self):
        return self.length

    def segregateEvenOdd(self):
        evens = LinkedList()
        evensInd = 0
        odds = LinkedList()
        oddsInd = 0
        curr = self.head
        while (curr != None):
            num = curr.data
            if num % 2 == 0:
                evens.insert(num, evensInd)
                evensInd += 1
            else:
                odds.insert(num, oddsInd)
                oddsInd += 1
            curr = curr.next
        return evens, odds


original = LinkedList()
original.insert(2, 0)
original.insert(3, 1)
original.insert(4, 2)
original.insert(1, 3)
original.insert(5, 4)
evens, odds = original.segregateEvenOdd()
evens.printList()
odds.printList()
# evens: 2 -> 4
# odds: 3 -> 1 -> 5
