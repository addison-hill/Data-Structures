from double_link_list import DoublyLinkedList

# LIFO - Last in first out
# like a vertical stack of pancakes, you eat the first pancake not the one on bottom
# in stack you can either declare head as top or tail, doesnt matter. In this case we will say head is top and tail is bottom


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)

    def pop(self):
        return self.storage.remove_from_head()

    def len(self):
        return self.storage.length
