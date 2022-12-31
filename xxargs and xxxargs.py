# xxargs works with tuple.......
def add(*num):
    sum=0
    for x in num:
        sum=sum+x
    return sum
print(add(3,8))
print(add(3,8,9))
print(add(3,8,9,8))

# xxxargs work with dictionary...........

def dict(**msg):
    print(msg)
    print(msg["name"])

dict(id=109,name="Nazmul Haque")