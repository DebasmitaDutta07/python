n=int(input("enter ur num:"))
s=0
temp=n
while n>0:
	fact=1
	i=1
	r=n%10
	while i<=r:
		fact=fact*i
		i=i+1
	print(fact)
	s=s+fact
	n=n//10
if(s==temp):
	print("krishnamurthy")
else:
	print(" not krishnamurthy")
