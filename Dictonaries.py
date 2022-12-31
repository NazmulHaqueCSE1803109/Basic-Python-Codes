studentId={
    101: "Nazmul Haque", # key can be integer or string
    102: "Abdullah Al Mamun",  # value can be a list
    103: "Mizanur Rahman"
}
print(studentId.get(103,"Not a valid key"))
print(studentId.get(104,"Not a valid key"))