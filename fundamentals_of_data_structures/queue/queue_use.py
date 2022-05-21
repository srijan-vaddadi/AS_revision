import OOP_queue

queue1 = OOP_queue.MyQueue()

for x in range(0, 11):
    queue1.push(x)

for x in range(0, queue1.size()):
    print(queue1.pull())
