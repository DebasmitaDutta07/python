num1=int(input("enter a number"))
num2=int(input("enter second number"))
if num1>num2:
    dividend=num1
    divisor=num2
else:
    dividend=num2
    divisor=num1
while(divisor!=0):
    remainder=int(dividend/divisor)
    dividend=divisor
    divisor=remainder
print("GCD of",num1,"and",num2,"is",dividend)
