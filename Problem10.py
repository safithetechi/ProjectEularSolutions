import math

def isPrime(num):
    num2=math.sqrt(num)
    for i in range (int(num2),0,-1):
        if(num%i==0 and i!=1):
            return False
    return True

def main():

    sums=0
    for i in range(2,2000000):
        if(isPrime(i)):
            sums=sums+i

    print(sums)

    input()

main()
