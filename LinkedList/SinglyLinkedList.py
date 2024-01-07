class SinglyLinkedListNode:
    def __init__(self, val: int = 0, next_node: 'SinglyLinkedListNode' = None):
        self.value = val
        self.next = next_node


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self) -> bool:
        return self.head is None

    def size(self) -> int:
        return self.count

    def prepend(self, val: int) -> None:
        new_node = SinglyLinkedListNode(val)
        self.count += 1

        if self.is_empty():
            self.head = self.tail = new_node

        new_node.next = self.head
        self.head = new_node

    def append(self, val: int) -> None:
        new_node = SinglyLinkedListNode(val)
        self.count += 1

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def remove(self, val: int) -> None:
        if self.is_empty():
            return

        self.count -= 1

        if val == self.head.value:
            self.head = self.head.next
            return

        current_node = self.head.next
        prev_node = self.head
        while current_node is not None and current_node.value != val:
            current_node = current_node.next
            prev_node = prev_node.next

        prev_node.next = current_node.next

        if current_node.value == self.tail.value:
            self.tail = prev_node

    def display(self) -> None:
        if self.is_empty():
            print("Empty")
            return

        output = ""
        current_node = self.head
        while current_node is not None:
            output += "{0} -> ".format(current_node.value)
            current_node = current_node.next

        print(output + 'None')


if __name__ == '__main__':
    sll = SinglyLinkedList()

    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.append(4)

    sll.display()
    print(sll.size(), sll.tail.value)

    print('Remove 4')
    sll.remove(4)
    sll.display()
    print(sll.size(), sll.tail.value)

    print('Prepend 4')
    sll.prepend(4)
    sll.display()
    print(sll.size(), sll.tail.value)

