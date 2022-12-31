a =int(input("Enter the value of a : "))
b =int(input("Enter the value of b : "))

x=(lambda a,b:a*a + 2*a*b + b*b)(a,b)
print(x)