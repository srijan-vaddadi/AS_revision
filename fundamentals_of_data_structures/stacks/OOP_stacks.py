class MyStack:
    def __init__(self):
        self._stack = []
        self._max_size = 10

    def get_max_size(self):
        return self._max_size

    def size(self):
        return len(self._stack)

    def push(self, x):
        if self.size() >= self._max_size:
            print('Stack overflow')
        else:
            self._stack.insert(0, x)

    def pull(self):
        if self.size() == 0:
            print('Stack underflow')
        else:
            return self._stack.pop(0)

