from collections import  deque
bank=deque(["nazmul","abdullah","mizan"])
print(bank)
bank.popleft()
bank.popleft()
bank.popleft()
if not bank:
    print("queue is empty")
