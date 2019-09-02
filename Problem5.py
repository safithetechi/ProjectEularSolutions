#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def gcd(a,b):   # fix this and make it work for an entire array 
    if b==0:
        return 0
    else:
        return gcd(b,a %b)


def lcm(a,b):
    return (a*b/gcd(a,b))



def main():

    print(gcd(3,4))


main()
