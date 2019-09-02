#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

from collections import deque

def reverse(iter):
    d = deque()
    d.extendleft(iter)
    return ''.join(d)

def CheckPalin(str):
    checkRstr=reverse(str)
    if(int(str)==int(checkRstr)):
        return True
    return False

def main():

    temp1=0
    temp2=0
    for i in range(900,1000):
        for j in range(900,1000):
            temp1=i*j
            if(temp2<temp1 and CheckPalin(str(temp1))):
               temp2=temp1

    print(temp2)
    input()

main()
