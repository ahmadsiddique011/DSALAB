from collections import deque
open =["[", "{", "("]
close = ["]", "}", ")"]
class isvalid:
    def __init__(self):
        self.stack = deque()
    def push(self, val):
        self.stack.append(val)
    def pop(self):
        self.stack.pop()
    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            False
    def size(self):
        return len(self.stack)
    def is_match(self,p1, p2):
        if open == '[' and p2 == ']':
            return True
        if open == '(' and p2 == ')':
            return True
        if open == '{' and p2 == '}':
            return True
        return False

    def is_paren_balanced(self,Equation):
        for brackets in Equation:
            if brackets in open:
                self.push(brackets)
            elif brackets in close:
                position = close.index(brackets)
                if ((self.size() > 0) and (open[position] == self.stack[self.size() - 1])):
                    self.pop()
                else:
                    return " InValid Equation"
        if self.size() == 0:
            return "Valid Equation"
        else:
            return "InValid Equation"





s = isvalid()

Equation = input("Enter Equation: ")
print(s.is_paren_balanced(Equation))
print(s.stack)

