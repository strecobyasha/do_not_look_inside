class Node:

    def __init__(self, value):
        self.prev = None
        self.next = None
        self.val = value


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_start(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def add_to_end(self, value):
        new_node = Node(value)
        if self.head:
            self.tail.next = new_node
            new_node.prev = self.tail
        else:
            self.head = new_node
        self.tail = new_node

    def remove_head(self):
        if self.head and self.head.next:
            self.head.next.prev = None
            self.head = self.head.next
        else:
            self.head = None
            self.pointer = None

    def remove_tail(self):
        if self.tail and self.tail.prev:
            self.tail.prev.next = None
        else:
            self.head = None
            self.pointer = None

    def elements_from_start(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next

    def elements_from_end(self):
        current_node = self.tail
        while current_node:
            yield current_node
            current_node = current_node.prev


obj = LinkedList()
elements = []


def test_add_start():
    elements_to_add = ['c', 'b', 'a']
    elements.extend(elements_to_add[::-1])
    for element in elements_to_add:
        obj.add_to_start(element)

    assert elements == [el.val for el in list(obj.elements_from_start())]


def test_add_end():
    elements_to_add = ['d', 'e', 'f']
    elements.extend(elements_to_add)
    for element in elements_to_add:
        obj.add_to_end(element)

    assert elements == [el.val for el in list(obj.elements_from_start())]


def test_show_from_start():
    assert elements == [el.val for el in list(obj.elements_from_start())]


def test_show_from_end():
    assert elements[::-1] == [el.val for el in list(obj.elements_from_end())]


def test_remove_head():
    obj.remove_head()
    assert elements[1:] == [el.val for el in list(obj.elements_from_start())]


def test_remove_tail():
    obj.remove_tail()
    assert elements[1:-1] == [el.val for el in list(obj.elements_from_start())]
