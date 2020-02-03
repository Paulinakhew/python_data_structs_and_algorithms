class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x  # item
        self.next = None  # ref


class LinkedList:
    def __init__(self):
        self.head = None  # start_node

    def traverse_list(self):
        '''Print items stored in a linked list.'''
        # check whether the list is empty or not
        if self.head is None:
            print("List has no element")
            return
        else:
            n = self.head  # initialize var n with head variable
            while n is not None:
                # print the item stored at the current node
                print(n.val, " ")
                # set the value of n to the next node
                n = n.next

    def insert_at_start(self, data):
        '''Insert an item at the start of a linked list.

        Keyword arguments:
            data: (int) the value of the item that will be inserted
        '''
        new_node = ListNode(data)  # create an object of the ListNode class
        new_node.next = self.head  # set its next value to head
        self.head = new_node
