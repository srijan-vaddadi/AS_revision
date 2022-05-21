import OOP_stacks

stack1 = OOP_stacks.MyStack()

for x in range(0, 11):
    stack1.push(x)

stack1.push(20)
stack1.push(44)
stack1.push('hello')

for x in range(0, stack1.size()):
    print(stack1.pull())

stack1.pull()
