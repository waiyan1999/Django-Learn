class User:
    def __init__(self, name, level):
        self.name = name
        self.level = level
user = User("KOthet","Admin")
print(user.name)
print(user.level)