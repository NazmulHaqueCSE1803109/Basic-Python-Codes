n=input("Enter a text of numbers : ")
# 10 20 30 40
list =n.split() #10,20,30,40
sum=0

for num in list:
    sum +=int(num)
print("Sumation is : ",sum)

# word, letter,digit count from a text...........
nl=0
nd=0
nw=0
txt=input("Enter a text : ")
for x in txt:
    x=x.lower()
    if x>='a' and x<='z':
        nl +=1
    elif x>='0' and x<='9':
        nd +=1
    elif x==' ':
        nw +=1
print("No of Letter : ",nl)
print("No of digit : ",nd)
print("No of word : ",nw+1)