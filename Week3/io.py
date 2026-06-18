with open("users.csv","a", encoding="utf-8") as file:
    file.write("1,Alice,Engineer\n")


with open("users.csv","r", encoding="utf-8") as file:
    print(file.read())
