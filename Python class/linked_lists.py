# Today, we are actually going to be designing a list !!!


# ARRAY VS LIST

# Advantages over arrays
# 1) Dynamic size
#     2) Ease of insertion/deletion

#     Drawbacks:
#     1) Random access is not allowed. We have to access elements sequentially starting from the first node. So we cannot do binary search with linked lists efficiently with its default implementation. Read about it here.
#     2) Extra memory space for a pointer is required with each element of the list.

#     Representation:
#     A linked list is represented by a pointer to the first node of the linked list. The first node is called the head. If the linked list is empty, then the value of the head is NULL.
#     Each node in a list consists of at least two parts:
#     1) data
#     2) Pointer(Or Reference) to the next node

# Node class
class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize
        # next as null

# Linked List class


class LinkedList:

    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None


def example():
    # Start with the empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    '''
    Three nodes have been created.
    We have references to these three blocks as head,
    second and third

    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  | None |     | 2  | None |     |  3 | None |
    +----+------+     +----+------+     +----+------+
    '''

    llist.head.next = second  # Link first node with second

    '''
    Now next of first Node refers to second.  So they
    both are linked.

    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  | None |     |  3 | None |
    +----+------+     +----+------+     +----+------+
    '''

    second.next = third  # Link second node with the third node

    '''
    Now next of second Node refers to third.  So all three
    nodes are linked.

    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  |  o-------->|  3 | None |
    +----+------+     +----+------+     +----+------+
    '''


# # PRACTICE:
# Linked List Traversal
# In the previous program, we have created a simple linked list with three nodes. Let us traverse the created list and print the data of each node. For traversal, let us write a general-purpose function printList() that prints any given list.


# Linked List class contains a Node object
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

    def insert(self, data, index):
        self.length += 1
        newNode = Node(data)
        if index == 0:
            self.head = newNode

    def deleteIndex(self, index):
        self.length -= 1

    def deleteData(self, data):
        self.length -= 1

    def length(self):
        return self.length


# Questions for thought

# How can we store size in linked list? How can we find length on the go?

# How can we delete nodes in linked list? How does this change for beginning / middle / end of list?
        # given index, given key

# How can we insert nodes in linked list? How does this change for beginning / middle / end of list?

# How would we be able to traverse fowards and backwards in linked list?

# How might we organize non linear data? (Ex. children sitting in a circle)

# Recursively search an element in a linked list

# Detecting loops in a linked list?? Hare and tortoise method. Floyd's slow and fast pointers algorithm.

# How can we find the length of a cycle in a linked list?


# HOMEWORK:
# Fill out the rest of the linked list class:
#   - insert
#   - deleteData
#   - deleteIndex

# Think very creatively and write a function to detect cycles in a linked list
# return True if there is a cycle, False otherwise
# Refer to the end of the lecture video for hints

# Try to test your own code this week!
