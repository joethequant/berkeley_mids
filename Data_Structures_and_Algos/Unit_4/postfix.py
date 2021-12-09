
class ArrayStack:
    '''
    Stack class built on top of a python list. 
    '''

    def __init__(self) -> None:
        self._data = []
    
    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f'{self._data}'

    def __getitem__(self, k):
        return self._data[k]

    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, element):
        return self._data.append(element)
    
    def top(self):
        if self.is_empty():
            raise ValueError('Stack is Empty')
        return (self._data[-1])

    def pop(self):
        if self.is_empty():
            raise ValueError('Stack is Empty')
        return self._data.pop()


def postfix(line):
    '''
    calculate line. 

    line: a string that needs to be solved.
    '''
    stack = ArrayStack()
    line = line.split(' ')
    for x in line:
        x = x.replace( '\n', '')

        if x == ' ':
            None
        elif x == '+':
            if not stack.is_empty():
                stack.push(stack.pop() + stack.pop())
        elif x == '-':
            if not stack.is_empty():
                last = stack.pop()
                second = stack.pop()
                stack.push(second - last)
        elif x == '*':
            if not stack.is_empty():
                stack.push(stack.pop() * stack.pop())
        elif x == '/':
            if not stack.is_empty():
                denominator = stack.pop()
                numerator = stack.pop()
                stack.push(numerator / denominator)
        else:    
            stack.push(int(x))
    return round(stack[0], 2)


# Open file.
with open('input.txt') as f:
    contents = f.readlines()

#Loop through lines and solve.
result = []
for x in contents:
    result.append(postfix(x))

#output values to an ouput file.
output = open("output.txt", "w")
lines = output.writelines( [str(x) + "\n" for x in result])
output.close()

