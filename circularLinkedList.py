"""
    A script to implement and manipulate a circular LnkdLst.
    
    We keep track of all items in every way possible, along with the usual adding, searching and removing functionality.
    
    Using Doxygen-compatible docstrings and comments.  Using four-space indentation by convention.
    
    @author: Nathaniel Schmidt <schmidty2244@gmail.com>
    Modified on Thu, 24/06/2021
"""

class Node:
    """
    An abstract / custom type to represent data elements for the l{LnkdLst}.
    """
    
    def __init__ (self, data, prev, next, inList):
        """
            Constructor for the node.
            
            @param data: the input data to be initially entered into the node.
            @type data: int
            @param prev: the previous node
            @type prev: l{Node}
            @param next: the succeeding node
            @type next: l{Node}
            @param inList: a pointer to the list that the node is in.
            @type inList: l{LnkdLst}
        """
        
        # Assign fields
        self.data = data
        self.prev = prev
        self.next = next
        self.inList = inList

class LnkdLst:
    """
        A custom type to represent a linked list collated from previously-defined l{Node} objects.
    """
    
    def __init__ (self, first, last):
        """
            Constructor for the linked list.
            
            @param first: Pointer to first list element.
            @type first: l{Node}
            @param last: Pointer to last list element
            @type last: l{Node}
        """
        
        self.first = first
        self.last = last

def isEmpty (list):
    """
        Checks to see if a list has no elements by means of the first pointer.
        
        @param list: The list to check.
        @type list: l{LnkdLst}
    """
    return list.first == None

def newNode (value, list, prev, next):
    """
        Instantiates a new node object in memory without inserting it into anything.
        
        @param value: The data to be inserted into the new node.
        @type value: int
                @param list: The list to check.
        @type list: l{LnkdLst}
        @param prev: Pointer / reference to the node prior to the new one, if any - required for the l{Node} constructor.
        @type prev: l{Node}
        @param next: Pointer / reference to the node prior to the new one, if any - required for the l{Node} constructor.
        @type next: l{Node}
    """
    result = Node (value, prev, next, list)
    return result

def appendToEnd (list, value):
    """
        Adds a node to the end of a list.
        
        @param list: Pointer to the list being appended to.
        @type list: l{LnkdLst}
        @param value: The data for the new node.
        @type value: int
    """
    appendedNode = newNode (value, list, list.last, None)
    if not isEmpty (list):
        list.last.next = appendedNode
        list.last = appendedNode
    else:
        list.first = appendedNode
        list.last = appendedNode

def addToStart (list, value):
    """
        Adds a node to the start of a list.
        
        @param list: Pointer to the list being appended to.
        @type list: l{LnkdLst}
        @param value: The data for the new node.
        @type value: int
    """
    appendedNode = newNode (value, list, None, list.first)
    if not isEmpty (list):
        list.first.prev = appendedNode
        list.first = appendedNode
    else:
        list.first = appendedNode
        list.last = appendedNode

def findReqd (list, value):
    """
        Searches for the first instance of a requested list element matching the provided data value; and does not account for duplicates.
        
        @param list: Pointer to the list being appended to.
        @type list: l{LnkdLst}
        @param value: The data for the new node.
        @type value: int
    """
    current = list.first
    while current is not None:
        if current.data == value:
            return current
        current = current.next
    return None

def delNode (current):
    """
        deletes the previously-selected node as per the prior function.
        
        @param current: The selected node to be deleted.
        @type current: l{Node}
    """
    if current == None:
        return
    
    list = current.inList
    before = current.prev
    after = current.next
    
    # is there something before this node?
    if before is not None:
        before.next = current.next
    
    else:
        # nothing before... so was first
        list.first = after
    
    # is there something after this node?
    if after is not None:
        after.prev = current.prev
    else:
        # nothing after... so was last
        list.last = before

    # now delete... and remove any links out to make sure
    current.prev = None
    current.next = None
    
    del current

def insert_after (selectedNode, value):
    if selected_node == None:
        return
    
    list = selectedNode.inList
    added = newNode (value, list, selectedNode, selectedNode.next)
    selectedNode.next = added
    after = added.next
    if after is not None:
        after.prev = added
    else:
        list.last = added

def printNode (current):
    """
        Prints a single node.
    """
    
    if current is None:
        return
    
    print (current.data)

def printAll (list):
    """
        prints all nodes in the given list.
    """
    current = list.first
    while current is not None:
        printNode (current)
        current = current.next
    print (".")

def printAllBackwards (list):
    """
        Same thing as before but the other way around.
    """
    current = list.last
    while current is not None:
        printNode (current)
        current = current.prev
    print (".")

def sum (list):
    """
    Prints the total sum of data values.
    """
    result = 0
    current = list.first
    
    while current is not None:
        result += current.data
        current = current.next
    print ("Sum of node data values: ", result)

def length (list):
    """
        Prints the length of the given list.
    """
    result = 0
    current = list.first
    
    while current is not None:
        result += 1
        current = current.next
    print ("Length of list: ", result)

def main ():
    # Initialise an instantiated list
    l1 = LnkdLst (None, None)
    
    print ("Test: add to end of list: ")
    appendToEnd (l1, 40)
    appendToEnd (l1, 50)
    appendToEnd (l1, 60)
    print ("Nodes so far: ")
    printAll (l1)
    
    print ("Test: add to start")
    addToStart (l1, 30)
    addToStart (l1, 20)
    addToStart (l1, 10)
    print ("Nodes so far: ")
    printAll (l1)
    
    print ("Nodes listed in reverse: ")
    printAllBackwards (l1)
    
    sum (l1)
    length (l1)
    
    print ("Now let's find a specific value belonging to a node. ")
    nodeQuery = findReqd (l1, 40)
    delNode (nodeQuery)
    nodeQuery = findReqd (l1, 20)
    delNode (nodeQuery)
    
    print ("Let's check which nodes we have left now: ")
    printAll (l1)
    sum (l1)
    length (l1)

main ()