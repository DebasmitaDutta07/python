import math
def peterson(n):
    num = n
    sum = 0
    while n > 0:
        r= int(n % 10)
        fact=math.factorial(r)
        sum += fact
        n = int(n / 10)
    return (sum == num)
  
  
# Driver Code
n =int(input("enter a number"))
d=peterson(n)
if d==True:
    print("yes")
else:
    print("no")
