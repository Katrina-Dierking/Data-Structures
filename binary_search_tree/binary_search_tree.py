"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        pass
        # cur_node = self.value
        
        #start at root and loop until cur_node is None
        #compare value and cur_node
            #if value <= cur_node
                #if cur_node.left is None
                    #insert our value
                #else
                    #go left (update cur_node to be cur_node.left)
            #elif value > cur_node
                #if cur_node.right is None
                    #insert our value
                #else
                    #go right (update cur node to be cur_node.right)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #compare target_value to cur_value
            #1. sides == we return true
            #2  < go left
            #3  > go right
            #4  if can't go left/right (not found, return False)
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        #go right
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
         #1. Base case: no more nodes in subtree
        
        #2  Base case: 
        fn(self.value)
        if self.left is not None:
            #for each node with a left child, call the cb function on it
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)
         
        cur_node = self  
        fn(cur_node.value) 
        # stack = # nodes you need to backtrack to
        while cur_node.left:
            cur_node = cur_node.left
            fn(cur_node)
            #add it to the stack
        pass

    # Part 2 -----------------------

    def delete(self,value):
        pass
        #research like we did in contains
        
        #if nde at bottom level
            #update parent left/right = None
        #if node has only one child
            #parent.left/right = node.left/right
        #if node has two children
            #larger child becomes parent of its sibling
        #if the child then has two children, which becomes the parent
        
        
        
        
        
    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self:
        
            if self.left:
                #go left - recursive
                #calling recursion on itself continually creates an infinite loop
                self.left.in_order_print()
            #print
            if self.right:
                #go right
                self.right.in_order_print()
            pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        #use a queue
        #print current node
        #add left child to q
        #add right child to q
        
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        #use a stack
        #push some initial value(5) ? onto stack so while loop has something to use
        #while ???
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required
    

    

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BST(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
