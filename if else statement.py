mark=int(input("Enter mark : "))
n1=int(input("Enter first number : "))
n2=int(input("Enter second number : "))

# pass/fail
if mark>=33:
    print("pass")
else:
    print("fail")

# largest
if n1>=n2:
    print(n1," is the larger number")
else:
    print(n2, " is the larger number")

# Even/Odd
if mark%2==0:
    print("Even")
else:
    print("Odd")