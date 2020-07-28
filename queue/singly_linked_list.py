class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node
    def get_value(self):
        return self.value
    def get_next(self):
        return self.next_node
    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList: 
    # constructor with only the self attribute
    def __init__(self): 
    # setting up an empty list
        self.head = None
        self.tail = None
        self.length = 0

    def get_length(self):
        return self.length


    def add_to_head(self, value):
        # when the list is empty, the head and tail are the same

        new_node = Node(value, self.head)
        self.head = new_node    
        if self.length == 0:
            # if self.head is None and self.tail is None
            new_node = Node(value, self.head)
            self.head = new_node
            self.length += 1 

    def add_to_tail(self,value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
        else: 
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1
            
            
    def remove_head(self):
        # we need to think about empty vs non-empty lists
        # if there is no head, there is nothing to remove_head

        if self.head is None:
            return None

        # list with 1 node
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -=1
            return value

        # list with two or more nodes
        else:
            # point head to whatever the current node is
            self.head = self.head.get_next()
            self.length -=1


    def remove_tail(self):
        #1 empty list
        if self.head is None:
            return None

        #2. list with one element
        elif self.head == self.tail:
            value = self.tail.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value

        #3. list with two or more elements
        else:
            # start at the head since we can't go back from the tail to the previous node
            cur_node = self.head
            # loop through until we get to the node that is pointing to the tail (so we don't go too far)
            while cur_node.get_next() is not self.tail:
                cur_node = cur_node.get_next()

            # so we can return the value of the removed node, we need to save it to a variable
            value = self.tail.get_value()
            cur_node.set_next(None)
            self.tail = cur_node
            self.length -= 1
            return value
    


    def contains(self, value):
        #1. use a loop to iterate through the linked list
        cur_node = self.head
        while cur_node is not None:
            if value == cur_node.get_value():
                return True
            cur_node = cur_node.get_next()
        return False
      

    def get_max(self):
        # pulls out biggest value in list
        # iterate through all the elements
        # we need to keep track of a current node
        # we need a temp node
        # we have to start at the head
      
        cur_node = self.head
        cur_max = self.head.get_value()
        while cur_node is not None:
            if cur_node.get_value() > cur_max:
                cur_max = cur_node.get_value()
                # to prevent an infinite while loop
            cur_node = cur_node.get_next()
        return cur_max


    def find_middle(self):
        # doing this in one pass without using "length"
        mid_point = self.head
        end_point = self.head
        while end_point is not None or end_point.get.next() is not None:
            #while loop is skipping forward by one and by two
            mid_point = mid_point.get_next()
            end_point = end_point.get_next().get_next()

        return mid_point.value

ll = LinkedList()
ll.add_to_tail(1)
ll.add_to_tail(2)
ll.add_to_tail(3)
ll.add_to_tail(4)
ll.add_to_tail(5)
print(ll.find_middle())