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
#         self.items = []
        
#     def isEmpty(self):
#         return self.items == []
    
#     def push(self,item):
#         self.items.append(item)
        
#     def pop(self):
#         return self.items.pop()
    
#     def peek(self):
#         return self.items[len(self.items)-1]
    
#     def size(self):
#         return len(self.items)
    
class Stack:
    def __init__(self, LinkedList):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        pass

    def push(self, value):
        pass

    def pop(self):
        pass
