#Occuring words in a string
str=input("ENTER THE STRING : ")
words=str.split()
for word in words:
    x=str.count(word)
    print("Frequency of",word,"is",x)
