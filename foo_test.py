#!/bin/python
from math import floor
import doctest
# def foo():
#     print("hi there!")

# def is_palindrome(word):
#     p=False
#     for i in range(0,len(word)):
#         if word[i] == word[-(i+1)]:
#             p=True
#         else:
#             p=False
#     return p

# def is_palindrome_too(word):
#     if word[::1] == word[::-1]:
#         return True
#     else:
#         return False

def fibonacci(n):
    """Return fibonacci(n).
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(9)
    34
    >>> fibonacci(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >=0
    >>> fibonacci(151)
    Traceback (most recent call last):
        ...
    ValueError: n too big
    >>> fibonacci(1.5)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    """
    if n < 0:
        raise ValueError("n must be >=0")
    elif n>150:
        raise ValueError("n too big")
    if floor(n) !=n:
        raise ValueError("n must be exact integer")
    fib0=0
    fib1=1
    
    if n==0:
        return fib0
    elif n==1:
        return fib1
    for i in range(2,n+1):        
        tmp = fib0+fib1
        fib0=fib1
        fib1=tmp
    
    return fib1


# def fibonacci_too(n=150):
#     fib=[]
#     fib.append(0)
#     fib.append(1)
#     if n==0:
#         return tuple(fib)
#     elif n==1:
#         return tuple(fib)
#     while fib[-1] <= n:
#         fib.append(fib[-1]+fib[-2])
#     return tuple(fib)

# def copy(itlist):
#     clist=[]
#     for i in range(len(itlist)):
#         clist.append(itlist[-1-i])
#     return tuple(clist)

# def dic(itlist):
#     slownik={}
#     for i, j in enumerate(itlist):
#         slownik[i]=j
#     return slownik

# def bar(a=1, b=2):
#     """this function prints args only"""
#     print("args:", a,b)

if __name__ == "__main__":
    doctest.testmod()
    # foo()
    # print(is_palindrome("bla"))
    # print(is_palindrome("yey"))
    # print(is_palindrome_too("kajak"))
    # print(is_palindrome("babel"))
    # print(is_palindrome_too("bgzxdfglzdn"))
    # print(fibonacci(3))
    # print(fibonacci(5))
    # print(fibonacci_too(9))
    # print(fibonacci_too())
    # llist = ['p', 'y', 't', 'h', 'o', 'n']
    # print(copy(llist))
    # print(dic(llist))
    # bar()
    # d=dir(bar)
    # print(bar.__doc__)
