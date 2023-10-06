s=input()
l=len(s)
print(l)
for i in range(l-1,0,-1):
    if s[i]==" ":
        lastindex=i;
        break;
print(s[0],end=".")
for j in range(0,lastindex):
	if s[j]==" ":
	    print(s[j+1],end=".")
for z in range(lastindex+1,l):
	print(s[z],end="")

	
	
