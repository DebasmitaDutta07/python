import camelcase
p=camelcase.CamelCase()
mylist=[]
newlist=[]
n=int(input("enter total elemrnts in the list"))
print("enter the elements in the list")
for i in range(n):
    x=input("enter the name")
    mylist.append(x)
print(mylist)
for j in mylist:
    a=p.hump(j)
    newlist.append(a)
print(newlist)
