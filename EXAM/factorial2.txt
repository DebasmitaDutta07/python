#Use factorial as Probability format
import fact_style as f
def factorial(num1,num2):
    f.fact_style(num1,num2)
    i=1
    fact1=1
    fact2=1
    while(i<=num1):
        fact1=fact1*i
        i+=1
    while(i<=num1-num2):
        fact2=fact2*i
        i+=1
    fact3=fact1//fact2
    return fact3

n1=int(input("ENTER THE n : "))
n2=int(input("ENTER THE r : "))
x=factorial(n1,n2)
print(" = ",x)
