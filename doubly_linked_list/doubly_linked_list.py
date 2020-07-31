"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
        
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next
    
    def set_next(self, new_next = None):
        self.next = new_next
    
    def get_prev(self):
        return self.prev
    
    def set_prev(self, new_prev = None):
        self.prev = new_prev
            
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
        new_node = ListNode(value, prev=None, next=self.head)
        
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.set_prev(new_node)
            self.head = new_node
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    
    def remove_from_head(self):
        if self.head == None and self.tail == None:
            return None
        elif self.head.next is None:
            old_node = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return old_node
        else:
            old_node = self.head.value
            self.head = self.head.next
            self.head.prev.delete()
            self.length -= 1
            return old_node

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        cur_node = ListNode(value)

        if self.length == 0:
            self.head = cur_node
            self.tail = cur_node
        else:
            self.tail.next = cur_node
            cur_node.prev = self.tail
            self.tail = cur_node

        self.length += 1
        return cur_node

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail is None and self.head is None:
            return None
        value = self.tail.get_value()
        if self.tail is self.head:
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.get_prev()
            self.tail.set_next()
        self.length -= 1
        return value

            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.get_value())
       
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.get_value())

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        #if the list is empty
        if self.tail is None and self.head is None:
            return None

        #if the list only has 1 node
        elif self.tail is self.head:
            self.head = None
            self.tail = None
            self.length -= 1

        elif node is self.head:
            self.remove_from_head()
        
        elif node is self.tail:
            self.remove_from_tail()

        else:
            cur_node = self.head
            prev_node = None
            next_node = self.head.get_next()

            while cur_node is not node:
                prev_node = cur_node
                cur_node = next_node
                next_node = cur_node.get_next()
            
            prev_node.set_next(next_node)
            next_node.set_prev(prev_node)
            cur_node = None
            self.length -= 1
        

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
        #handle empty list
        if self.head is None:
            return None

        #keep track of current max
        cur_node = self.head
        cur_max = self.head.value
        #loop through
        while cur_node is not None:
            #compare current max with each value
            if cur_node.value > cur_max:
                cur_max = cur_node.value
            #update current node to prevent infinate loop
            cur_node = cur_node.next
        #return max
        return cur_max 