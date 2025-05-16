import pickle
class ToDo:
    def __init__(self, tilte, important, category = "Normal"):
        self.title = tilte
        self.important = important
        self.category = category
todos = [ToDo("Ride bike",True),ToDo("drink milk", False),ToDo("Learn Python", True, category="work")]

file = open("txt.txt", "wb")
pickle.dump(todos, file)
file.close()

file = open("txt.txt","rb")
todods = pickle.load(file)
file.close()
print(todods)
