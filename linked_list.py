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
            data: (int) the value of the item that will be inserted at the start
        '''
        new_node = ListNode(data)  # create an object of the ListNode class
        new_node.next = self.head  # set its next value to head
        self.head = new_node

    def insert_at_end(self, data):
        '''Insert an item at the end of a linked list.

        Keyword arguments:
            data: (int) the value of the item that will be inserted at the end
        '''
        new_node = ListNode(data)  # create an object of the ListNode class
        if self.head is None:  # if there isn't an existing linked list
            self.head = new_node  # set the value of head to new_node
            return
        n = self.head  # initialize n with head node
        while n.next is not None:  # iterate through nodes in list
            n = n.next
        n.next = new_node  # set reference of last node to new_node

    def insert_after_item(self, x, data):
        '''Add item after another item in a linked list.

        Keyword arguments:
            x: (int) number after which you want to insert the new node
            data: (int) the value for the new node
        '''
        n = self.head
        print(n.next)
        while n is not None:
            if n.val == x:  # break loop if the current node is equal to x
                break
            n = n.next
        if n is None:  # only occurs if the item is not found
            print("item not in the list")
        else:
            new_node = ListNode(data)
            new_node.next = n.next
            n.next = new_node
