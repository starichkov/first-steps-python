class Animal:
    # "constructor"
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("What does the fox say?!")

    @classmethod
    def class_method(cls, text):
        print(text)

    @staticmethod
    def static_method(text):
        print(text)


class Cat(Animal):
    # class ("static") variable
    legs = 4

    # "toString()"
    def __repr__(self):
        return "Cat { name = " + self.name + " }"

    # override method from superclass
    def make_sound(self):
        # call method's realization from superclass
        super().make_sound()
        print(self.name + " says meow!")


cat = Cat("Alice")
print(cat)

cat.make_sound()
print("Cat has {} legs. {}!".format(cat.legs, Cat.legs))

Animal.class_method("This is a class method!")
Animal.static_method("This is a static method!")
