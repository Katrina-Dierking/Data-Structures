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
        if value < self.value:
            if not self.left:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BST (value)
            else:
                self.right.insert(value)

    def contains(self, target):
        #compare target_value to cur_value
            #1. sides == we return true
            #2  < go left
            #3  > go right
            #4  if can't go left/right (not found, return False)
        if target == self.value:
            return True
        if target < self.value:
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        #go right
        current = self
        max_value = self.value
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value

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
