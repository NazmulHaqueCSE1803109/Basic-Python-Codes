# use of break....
bp=int(input("Enter breaking point : "))
i=1
while i<=100:
    if i==bp:
        break;
    print(i,end=" ")
    i +=1
print("\nend")

# uses of continue .........
i=1
n=int(input("Enter the value of n : "))
while i<=n:
    print(i, end=" ")
    i += 1
    if i%2==0:
        continue

print("\nend program")