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

    def insert_before_item(self, x, data):
        if self.head is None:  # check if list is empty
            print("List has no element")
            return
        if x == self.head.val:  # if the element is located at first index
            new_node = ListNode(data)
            new_node.next = self.head
            self.head = new_node
            return
        n = self.head
        print(n.next)
        while n.next is not None:
            if n.next.val == x:
                break
            n = n.next
        if n.next is None:
            print("item not in the list")
        else:
            new_node = ListNode(data)
            new_node.next = n.next
            n.next = new_node

    def insert_at_index(self, index, data):
        if index == 0:
            new_node = ListNode(data)
            new_node.next = self.head
            self.head = new_node
        i = 0
        n = self.head
        while i < index - 1 and n is not None:
            n = n.next
            i += 1
        if n is None:
            print("Index out of bound")
        else:
            new_node = ListNode(data)
            new_node.next = n.next
            n.next = new_node

    def get_count(self):
        if self.head is None:
            return 0
        n = self.head
        count = 0
        while n is not None:
            count += 1
            n = n.next
        return count

    def search_item(self, x):
        if self.head is None:
            print("List has no elements")
            return
        n = self.head
        while n is not None:
            if n.val == x:
                print("Item found")
                return True
            n = n.next
        print("Item not found")
        return False

    def make_new_list(self):
        nums = int(input("How many nodes do you want to create: "))
        if nums == 0:
            return
        for num in range(nums):
            value = int(input("Enter the value for the node: "))
            self.insert_at_end(value)

    def delete_at_start(self):
        if self.head is None:
            print("The list has no element to delete")
            return
        self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            print("The list has no element to delete")
            return
        n = self.head
        while n.next.next is not None:
            n = n.next
        n.next = None

    def delete_element_by_value(self, x):
        if self.head is None:
            print("The list has no element to delete")
            return
        if self.head.val == x:
            self.head = self.head.next
            return
        n = self.head
        while n.next is not None:
            if n.next.val == x:
                break
            n = n.next
        if n.next is None:
            print("item not found in the list")
        else:
            n.next = n.next.next

    def reverse_linkedlist(self):
        prev = None
        n = self.head
        while n is not None:
            next = n.next
            n.next = prev
            prev = n
            n = next
        self.head = prev


if __name__ == "__main__":
    ll = LinkedList()
    ll.make_new_list()
    ll.traverse_list()
