file=open("text.txt","r")
test=file.read()
print(test)
size=len(test)
print(size)
test1=file.readlines()
print(test1)

file.close()