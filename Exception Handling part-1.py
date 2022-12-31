try:
    list=[10,0,20]
    result=list[0]/list[3]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Divided by zero is not possible")
except IndexError:
    print("Index Error")
finally:
    print("Successful")