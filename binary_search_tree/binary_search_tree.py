from dll_stack import Stack
from dll_queue import Queue
# import sys
# sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if value < self.value look left
        if value < self.value:
            # if something is there already
            if self.left:
                # recurse left
                self.left.insert(value)
            # if not
            else:
                # insert left
                self.left = BinarySearchTree(value)

        # if value >= self.value look right
        if value >= self.value:
            # if something is there already
            if self.right:
                # recurse right
                self.right.insert(value)
            # if not
            else:
                # insert right
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not

    # if node is none:
    #  return false
    # if node.value == findvalue:
        # return true
    # else:
    #      if find < node.value:
              # find on left node
         # else
            # find on right node

    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        if target >= self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    # follow the right until the end, the max is the right most node
    # if theres a right:
    #   get max on right
    # else - return node.value

    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # call cb on self.value
        cb(self.value)
        # if left
        if self.left:
            # call for_each
            self.left.for_each(cb)
        # if right
        if self.right:
            # call for_each
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    # values from low to high ---> left node | node | right node
    def in_order_print(self, node):
        if node.left != None:
            self.in_order_print(node.left)

        print(node.value)

        if node.right != None:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # Iterative BFT
    # create queue
    # add root to queue
    # while queue is not empty
    # node = pop head of queue
    # DO THE THING!!! (print)
    # add children of node to queue

    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    # Iterative DFT
    # create stack
    # add root to stack
    # while stack is not empty
    # node = pop top of stack
    # DO THE THING!!! (print)
    # add children of node to stack

    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
