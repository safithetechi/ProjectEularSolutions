def GenerateNumbers(start,end):
    ListOfNumbers=[]
    for i in range(start,end):
        ListOfNumbers.append(i)
    return ListOfNumbers

#------------------------------Eulers Sieve-------------------------------------------------------

#Make this faster, right now it is in n^2+n
#Not Finished
def EulersSieve(n):

    temp=GenerateNumbers(2,n)
    temp2=[]
    Ans=[]
    for i in range(0,len(temp)):
        temp2.append(temp[i])
        for j in range(i+1,len(temp)):
            if(temp[j]%temp[i]!=0):
                temp2.append(temp[j])

        print(temp2)
    return Ans
#-------------------------------------------------------------------------------------------------

def isPrime(num):
    num2=math.sqrt(num)
    for i in range (int(num2),0,-1):
        if(num%i==0 and i!=1):
            return False
    return True





