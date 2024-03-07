class Student:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print("hello ", self.name)

class Polygon:

    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        perimeter = sum(self.sides)
        return perimeter

if __name__ == '__main__':

    Student("Arish").say_hello()

    #Student1  is the instance variable
    student1  = Student("Joe")
    student1.say_hello()

    polygon1 = Polygon(sides=[5,3,2])
    print(polygon1.perimeter())
    polygon2 = Polygon(sides=[7,9,13,11,17])
    print(polygon2.perimeter())