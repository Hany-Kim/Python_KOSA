# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def fibo1(n):
    print("========================")
    a, b = 0, 1
    while b<n:
        print(b, end=' ')
        a, b = b, a+b
    print()
    
def fibo2(n):
    result = []
    a, b = 0, 1
    while b<n:
        result.append(b)
        a, b = b, a+b
    return result

if __name__ == "__main__" :
    import sys
    fibo1(int(sys.argv[1]))