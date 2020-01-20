class Person:
    def __init__(self, name):
        self.name = name
        self.greet()


    def greet(self):
        print('Hello, I am {}!'.format(self.name))


pers = Person(input())
