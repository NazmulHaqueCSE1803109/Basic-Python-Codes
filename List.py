subjects=["c","c++","java","python","html","css"]
print(subjects[0])
print(subjects[1])
print(subjects[-1])
print(subjects[-2])
print("c++" in subjects)
print("c" not in subjects)
print(subjects+["swift",27])
print(len(subjects))
subjects.append("javascript")
print(subjects)
subjects.remove("javascript")
print(subjects)
subjects.sort()
print(subjects)
subjects.reverse()
print(subjects)
ind=subjects.index("c++")
print(ind)
subjects1=subjects.copy()
print(subjects1)
subjects1.pop()
print(subjects1)
subjects1.clear()
print(subjects1)
cnt=subjects.count("c")
print(cnt)