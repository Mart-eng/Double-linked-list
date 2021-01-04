# ListNode2.py

class ListNode2:
    
    def __init__(self, item = None, leftL = None, rightL = None):

        '''creates a ListNode with the specified data value and
           two links: to the previous node and to the next node
        post: creates a ListNode with the specified data value and links'''
        
        self.item = item
        self.leftL = leftL
        self.rightL = rightL

    def __str__(self):
      ''' for printing the node '''
      
      return str(self.item)

def printLR(headNode):
    """ prints all elements following right links, starting with the headNode """
    node = headNode
    
    while node is not None:
        print(node.item, end = "\t")
        node = node.rightL

    print("end of linked list")

def printRL(tailNode):
    """ generates a list all elements following left links,
    starting with the tailNode """
    
    node = tailNode
    listV = []
    
    while node is not None:
        listV.append(node.item)
        node = node.leftL
    
    listV = listV[::-1]
    print("here is the list of elements, following left links:",listV)

    return listV
        
           

# Testing
# create a linked list of 5 values: 34, 1, 23, 7, and 10.
# Displays it.

# put the code here, make n1 to be 34, and n5 be 10

n5 = ListNode2(10)
n4 = ListNode2(7, rightL = n5)
n5.leftL = n4

n3 = ListNode2(23, rightL = n4)
n4.leftL = n3

n2 = ListNode2(1, rightL = n3)
n3.leftL = n2

n1 = ListNode2(34, rightL = n2)
n2.leftL = n1


### printing all the nodes, one by one, following right links, then left links
printLR(n1)
printRL(n5)


### Then insert new value, say 8 between 34 and 1. Display the updated list
print()
print("Inserting 8...")

### put the code here
n6 = ListNode2(8,n1,n2)
n1.rightL = n6
n2.leftL = n6

printLR(n1)
printRL(n5)

             
# Then delete node with value 7, update the links and display the new list.

print("Deleting 7...")

# put the code here
n3.rightL = n5
n5.leftL = n3

printLR(n1)
printRL(n5)
