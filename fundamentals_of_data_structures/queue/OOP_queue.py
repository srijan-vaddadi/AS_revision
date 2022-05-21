class MyQueue:
    def __init__(self):
        self._queue = []

    def push(self, x):
        self._queue.append(x)

    def pull(self):
        return self._queue.pop(0)

    def size(self):
        return len(self._queue)
