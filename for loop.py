num=[10,20,30,40,50,60,70,80,90,100]
print(num,end=" ")
print("\n")
sum=0
for x in num:
    sum +=x
print("sumation : ",sum)

# 1+2+.......+n
n=int(input("Enter the value of n : "))
sum=0
for x in range(1,n+1,1):
    sum +=x
print(sum)

# 2+4+.......+n
n=int(input("Enter the value of n : "))
sum=0
for x in range(2,n+1,2):
    sum +=x
print(sum)

# 1+3+.........+n
n=int(input("Enter the value of n : "))
sum=0
for x in range(1,n+1,2):
    sum +=x
print(sum)

# 1*1+2*2+.........+n*n
n=int(input("Enter the value of n : "))
sum=0
for x in range(1,n+1,1):
    sum +=(x*x)
print(sum)

# Find factorial value
n=int(input("Enter the value of n : "))
sum=1
for x in range(1,n+1,1):
    sum *=x
print(sum)