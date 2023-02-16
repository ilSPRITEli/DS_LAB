class ArrayStack():
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)
        return self.stack
    
    def pop(self):
        return self.stack.pop()
    
    def stackTop(self):
        return self.stack[-1]
    
    def printStack(self):
        print(self.stack)

def is_parentheses(txt):
    stack = ArrayStack()
    for i in txt:
        if i == '(':
            stack.push(i)
        elif i == ')':
            if not stack.is_empty():
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False
    
def copyStack(stack, new_stack):
    while not stack.is_empty():
        new_stack.push(stack.pop())

def InfixToPostfix(txt):
    opp = {'+':1, '-':1, '*':2, '/':2}
    wow = ArrayStack()
    opp_stack = ArrayStack()
    for i in txt:
        if (i in opp and opp_stack.is_empty()) or (i in opp and opp[i] > opp[opp_stack.stackTop()]):
            opp_stack.push(i)
        elif i in opp and opp[i] <= opp[opp_stack.stackTop()]:
            while opp[i] <= opp[opp_stack.stackTop()]:
                wow.push(opp_stack.stackTop())
                opp_stack.pop()
                if opp_stack.is_empty():
                    opp_stack.push(i)
                    break
        else:
            wow.push(i)
    while not opp_stack.is_empty():
        wow.push(opp_stack.stackTop())
        opp_stack.pop()
    print("".join(wow.stack))

InfixToPostfix("A+B*C-D/E")
