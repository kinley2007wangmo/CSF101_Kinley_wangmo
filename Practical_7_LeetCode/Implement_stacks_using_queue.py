from queue import Queue

class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        self.q2.put(x)
        while not self.q1.empty():
            self.q2.put(self.q1.get())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.get()

    def top(self) -> int:
        return self.q1.queue[0]

    def empty(self) -> bool:
        return self.q1.empty()

# Example test cases
stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())    # Output: 2
print(stack.pop())    # Output: 2
print(stack.empty())  # Output: False
