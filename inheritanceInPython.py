class Animal():
    def move(self):
        print("I am animal I can move")

class Human(Animal):
    def move(self):
        print("I am human I can walk and run")

class Snake(Animal):
    def move(self):
        print("I am snake I can slither")

#Parent class
class Bird():
    def __init__(self):
        print("Bird is ready")
    def WhoIsThis(self):
        print("Bird")

    def fly(self):
        print("Fly higher")

    def swim(self):
        print("Swim faster")

class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")

    def WhoIsThis(self):
        print("Penguin")


