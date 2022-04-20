# Node of a doubly linked list
class Node:
    def __init__(self, data):
        self.next = None  # reference to next node in DLL
        self.prev = None  # reference to previous node in DLL
        self.data = data


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # This function prints contents of linked list
    # starting from head
    def printList(self):
        temp = self.head
        while (temp != None):
            print(temp.data)
            temp = temp.next

    # Add a node at the end of the DLL
    def append(self, new_data):
        newNode = Node(new_data)
        if self.length == 0:
            self.length += 1  # Vijay
            self.head = newNode
            self.tail = newNode
            return

        if self.length == 1:
            self.length += 1
            self.tail = newNode
            self.head.next = newNode   # Sai
            newNode.prev = self.head
            return

        self.length += 1
        tmp = self.tail
        tmp.next = newNode
        newNode.prev = tmp   # Meenakshi
        self.tail = newNode

    def length(self):
        return self.length

    def isPalindrome(self):
        pass


racecar = LinkedList()
racecar.append('R')
racecar.append('A')
racecar.append('C')
racecar.append('E')
racecar.append('C')
racecar.append('A')
racecar.append('R')
racecar.printList()
