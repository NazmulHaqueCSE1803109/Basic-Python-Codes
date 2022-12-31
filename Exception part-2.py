try:
    list=[10,0,20]
    div=list[0]/list[1]
    print(div)
    print("Done")
except (ValueError,ZeroDivisionError,IndexError):
    print("You have entered incorrect input.")
finally:
    print("Thanks!!!")

# Create Exception........

def voter(age):
    if age<18:
        raise ValueError("Invalid Voter")
    return "You are allowed to vote"
try:
    print(voter(19))
    print(voter(12))
except ValueError as e:
    print(e)