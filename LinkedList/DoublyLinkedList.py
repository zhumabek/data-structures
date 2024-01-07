class ListNode:
    def __init__(self, val: int, next_node: 'ListNode' = None, prev_node: 'ListNode' = None):
        self.value = val
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self) -> bool:
        return self.head is None

    def size(self) -> int:
        return self.count

    def append(self, val: int):
        new_node = ListNode(val)
        self.count += 1

        if self.is_empty():
            self.head = self.tail = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def prepend(self, val: int):
        new_node = ListNode(val)
        self.count += 1

        if self.is_empty():
            self.head = self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def remove(self, val: int):
        if self.is_empty():
            return

        self.count -= 1

        if val == self.head.value:
            new_head = self.head.next

            if new_head is None:
                self.head = None
                self.tail = None
            else:
                new_head.prev = None
                self.head = new_head

            return

        current_node = self.head
        while current_node is not None and current_node.value != val:
            current_node = current_node.next

        prev_node = current_node.prev
        if current_node == self.tail:
            prev_node.next = None
            self.tail.prev = None
            self.tail = prev_node

        else:
            prev_node.next = current_node.next
            current_node.next.prev = prev_node

    def display(self) -> None:
        if not self.head:
            print('Empty')
            return

        output = ""
        current_node = self.head
        while current_node is not None:
            output += "{0} -> ".format(current_node.value)
            current_node = current_node.next

        print(output + 'None')


if __name__ == '__main__':
    dll = DoublyLinkedList()

    dll.append(23)
    dll.append(13)
    dll.append(63)

    dll.display()
    print("size: {0}, head: {1}, tail: {2} ".format(dll.size(), dll.head.value, dll.tail.value))

    dll.prepend(45)
    dll.display()
    print("size: {0}, head: {1}, tail: {2} ".format(dll.size(), dll.head.value, dll.tail.value))

    dll.remove(63)
    print('Remove 63')
    dll.display()
    print("size: {0}, head: {1}, tail: {2} ".format(dll.size(), dll.head.value, dll.tail.value))

    dll.prepend(63)
    print('Prepend 63')
    dll.display()
    print("size: {0}, head: {1}, tail: {2} ".format(dll.size(), dll.head.value, dll.tail.value))

