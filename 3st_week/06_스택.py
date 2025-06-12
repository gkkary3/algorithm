class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        next_head = Node(value)
        next_head.next = self.head
        self.head = next_head
        return

    # pop 기능 구현
    def pop(self):
        if self.is_empty():
            return "Stack is empty!"
        del_node = self.head
        self.head = self.head.next
        return del_node

    def peek(self):
        if self.is_empty():
            return "Stack is empty!"
        # 맨 위의 데이터 반환
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None