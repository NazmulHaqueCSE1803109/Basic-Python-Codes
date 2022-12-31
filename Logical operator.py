# Finding Largest number

n1=int(input("first number : "))
n2=int(input("second number : "))
n3=int(input("third number : "))

if n1>=n2 and n2>=n3:
    print(n1 ," is the largest number")
elif n2>=n1 and n1>=n3:
    print(n2, " is the largest number ")
else:
    print(n3," is the largest number")

# Test vowel consonant
ch=input("Enter a character : ")
if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
    print("vowel")
else:
    print("consonat")