import pytest
import linked_list as l


def test_create_linked_list():
    new_linked_list = l.LinkedList()
    assert new_linked_list


def test_create_and_insert_single_value_into_linked_list():
    new_linked_list = l.LinkedList()
    new_linked_list.insert_at_start(20)
    assert new_linked_list
    assert new_linked_list.head.val == 20


def test_create_and_insert_multiple_values_into_linked_list():
    new_linked_list = l.LinkedList()
    new_linked_list.insert_at_start(1)
    new_linked_list.insert_at_start(2)
    new_linked_list.insert_at_start(3)
    new_linked_list.insert_at_start(4)
    new_linked_list.insert_at_start(5)
    assert new_linked_list
    assert new_linked_list.head.val == 5
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 4
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 3
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 2
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 1
