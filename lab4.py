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
                print("Parentheses in %s are unmatched" %txt)
                return False
    if stack.is_empty():
        return True
    else:
        print("Parentheses in %s are unmatched" %txt)
        return False
    
def copyStack(stack, new_stack):
    while not new_stack.is_empty():
        new_stack.pop()
    for i in stack.stack:
        new_stack.push(i)
    return new_stack
def InfixToPostfix(txt):
    opp = {'+':1, '-':1, '*':2, '/':2}
    wow = ''
    opp_stack = ArrayStack()
    for i in txt:
        if (i in opp and opp_stack.is_empty()) or (i in opp and opp[i] > opp[opp_stack.stackTop()]):
            opp_stack.push(i)
        elif i in opp and opp[i] <= opp[opp_stack.stackTop()]:
            while opp[i] <= opp[opp_stack.stackTop()]:
                wow += opp_stack.stackTop()
                opp_stack.pop()
                if opp_stack.is_empty():
                    break
            opp_stack.push(i)
        else:
            wow += i
    while not opp_stack.is_empty():
        wow += opp_stack.stackTop()
        opp_stack.pop()
    print('Postfix of %s is %s' %(txt, wow))

# txt = "((A-B)))*C)"
# result = is_parentheses(txt)
# print(result)

s1 = ArrayStack(); s1.push(10); s1.push(20); s1.push(30)
s2 = ArrayStack(); s2.push(15)
copyStack(s1, s1)

s1.printStack()
s2.printStack()


InfixToPostfix("A+B*C/D-F")