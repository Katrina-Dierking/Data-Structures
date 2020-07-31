"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
        
#     def __len__(self):
#         return self.size
    
#     def push(self, value):
#         self.storage.append(value)
#         self.size += 1
        
#     def pop(self):
#         if self.size == 0:
#             return None
#         else:
#             self.size -= 1
#             return self.storage.pop()
        
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return f'{self.value}, {self.next}'
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
        
    def push(self, value):
        if self.head == None:
            self.head = Node(value)
            
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            
    def pop(self):
        if self.isempty():
            return None
        else:
            oldNode = self.head
            self.head = self.head.next
            oldNode.next = None
            return oldNode.value
        
    def getcount(self):
        temp_node = self.head
        count = 0
        while temp_node:
            count += 1
            temp_node = temp_node.next
        return count
    
    def __str__(self):
        return f'{self.head}'
    
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.push(value)
        self.size = self.storage.getcount()

    def pop(self):
        value = self.storage.pop()
        self.size = self.storage.getcount()
        return value


stack = Stack()
stack.push(100)
stack.push(101)
stack.push(105)


stack.pop()

