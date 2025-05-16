import sys
file_name = "todo_data.txt"
todos = []
#read file
try:
    file = open(file_name, "r")
    todos = file.readlines()
    file.close()
except:
    pass
print(todos)
