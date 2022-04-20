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

    #r a c e c a r
    

    def palindrome(self):
        head = self.head #r
        tail = self.tail #r 
        steps = 0
        print(tail.data, head.data)

        while head.data == tail.data and steps != self.length//2:
            tail = tail.prev
            head = head.next
            steps += 1
            

        if steps != self.length // 2:
            return False
        else:
            return True
            


racecar = LinkedList()
racecar.append('R')
racecar.append('A')
racecar.append('C')
racecar.append('E')
racecar.append('C')
racecar.append('A')
racecar.append('R')
racecar.printList()

print(racecar.palindrome())

apple = LinkedList()
apple.append('A')
apple.append('P')
apple.append('P')
apple.append('L')
apple.append('E')

print(apple.palindrome())

appa = LinkedList()
appa.append('a')
appa.append('p')
appa.append('p')
appa.append('a')

print(appa.palindrome())