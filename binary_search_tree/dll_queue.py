from double_link_list import DoublyLinkedList


# FIFO - First in First out


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements? Because we need to add to tail, remove from head
        self.storage = DoublyLinkedList()

    def enqueue(self, value):  # entering the queue or entering at back of line, aka add to tail
        self.storage.add_to_tail(value)

    def dequeue(self):  # remove from queue, so this will be like front of line, aka remove from head
        return self.storage.remove_from_head()

    def len(self):
        return self.storage.length
