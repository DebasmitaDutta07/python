a=list(map(int,input().split()))
print(a)
max=0
for i in a:
        for j in a:
	t=j-i
	if t>max:
                        max=t
print(max)
