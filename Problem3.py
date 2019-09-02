import math

def isPrime(num):
    num2=math.sqrt(num)
    for i in range (int(num2),0,-1):
        if(num%i==0 and i!=1):
            return False
    return True

def main(num):
    num2=math.sqrt(num)
    for i in range (int(num2),0,-1):
        if(num%i==0 and isPrime(i)):
            print(i)
            break

main(600851475143)
