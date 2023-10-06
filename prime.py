def isPrime(num):
    count=0
    for i in range (1,num+1):
        if num%i==0:
            count=count+1
    if count==2:
        print("prime")
    else:
        print("not prime")
n=int(input("enter a number"))
isPrime(n)
    
