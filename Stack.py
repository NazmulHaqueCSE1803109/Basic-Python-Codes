books=[]
books.append("Learn C")
books.append("Learn C++")
books.append("Learn Java")

print(books)
books.pop()
print("now top element is : ", books[-1])
books.pop()
print("now top element is : ", books[-1])
books.pop()
print(books)
if not books:
    print("No books left")