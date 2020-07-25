"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        pass
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    
    def remove_from_head(self):
        if self.length == 0:
            # return undefined
            old_head = self.head

        elif self.length ==1:
            self.head is None
            self.tail is None

        else:
            self.head = old_head.next
            self.head.prev is None
            old_head.next is None
            
            self.length -=1
            # return old_head

   
    

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        cur_node = ListNode(value)

        if self.length is None:
            self.head = cur_node
            self.tail = cur_node
        else:
            self.tail.next = cur_node
            cur_node.prev = self.tail
            self.tail = cur_node

            self.length += 1
            # return cur_node

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.head == 0:
            return None
        
        else:
            old_tail = self.tail
            self.tail = old_tail.prev
            self.tail.next = None	
            old_tail.prev = None
        
            self.length -= 1
            # return old_tail
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        cur_node = self.head
        while cur_node != node:
            cur_node = cur_node.next

            cur_node.prev.next = cur_node.next
            cur_node.next.prev = cur_node.prev

    # a way to do it without a loop because we are passing in a node not a value
    #  def delete(self, node: ListNode):
    #     node.prev.next = node.next 
    # -- look at what comes after node and set its prev pointer = 
    #     to original node's prev pointer
    #     node.next.prev = node.prev



    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        cur_node = self.head
        cur_max = self.head.value
        while cur_node is not None:
            if cur_node.value > cur_max:
                cur_max = cur_node.value
            cur_node = cur_node.next
        return cur_max 