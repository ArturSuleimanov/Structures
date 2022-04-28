'''
Describing of stack(last in, first out) structure
>>> clear()
>>> is_empty()
True
>>> push(1)
>>> push(2)
>>> push(3)
>>> is_empty()
False
>>> pop()
3
>>> pop()
2
>>> pop()
1
>>> is_empty()
True
'''


_stack = []  
def push(x):    # adding element to the end
    _stack.append(x)

def pop():
    x = _stack.pop()    # taking last element
    return x

def clear():    # clearing stack
    _stack.clear()


def is_empty():    # checking if stack is empty
    return len(_stack) == 0



if __name__ ==  '__main__':
    import doctest
    doctest.testmod()



