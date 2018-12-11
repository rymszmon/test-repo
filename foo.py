#!/bin/python
from math import floor
def foo():
    print("hi there!")

def is_palindrome(word):
    p=False
    for i in range(0,len(word)):
        if word[i] == word[-(i+1)]:
            p=True
        else:
            p=False
    return p

def is_palindrome_too(word):
    if word[::1] == word[::-1]:
        return True
    else:
        return False

def fibonacci(n):
    fib=[]
    fib.append(0)
    fib.append(1)
    if n==0:
        return tuple(fib)
    elif n==1:
        return tuple(fib)
    for i in range(2,n+1):        
        fib.append(fib[i-1]+fib[i-2])
    return tuple(fib)

def fibonacci_too(n=150):
    fib=[]
    fib.append(0)
    fib.append(1)
    if n==0:
        return tuple(fib)
    elif n==1:
        return tuple(fib)
    while fib[-1] <= n:
        fib.append(fib[-1]+fib[-2])
    return tuple(fib)

def copy(itlist):
    clist=[]
    for i in range(len(itlist)):
        clist.append(itlist[-1-i])
    return tuple(clist)

def dic(itlist):
    slownik={}
    for i, j in enumerate(itlist):
        slownik[i]=j
    return slownik

def bar(a=1, b=2):
    """this function prints args only"""
    print("args:", a,b)

if __name__ == "__main__":
    foo()
    print(is_palindrome("bla"))
    print(is_palindrome("yey"))
    print(is_palindrome_too("kajak"))
    print(is_palindrome("babel"))
    print(is_palindrome_too("bgzxdfglzdn"))
    print(fibonacci(3))
    print(fibonacci(5))
    print(fibonacci_too(9))
    print(fibonacci_too())
    llist = ['p', 'y', 't', 'h', 'o', 'n']
    print(copy(llist))
    print(dic(llist))
    bar()
    d=dir(bar)
    print(bar.__doc__)