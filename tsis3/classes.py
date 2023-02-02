import math


class NewString:
    def __init__(self, s):
        self.s = s

    def printstring(self):
        print(self.s.upper())


class Shape:
    def __init__(self, length=0):
        self.length = length


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print(self.length * self.length)


class Reactangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.width * self.length)


class Point:
    def __init__(self,x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self,x, y):
        self.x = x
        self.y = y

    def dist(self, x, y):
        return math.sqrt(((x - self.x)**2) + ((y - self.y)**2))


class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Insufficient Funds")
        else:
            self.balance = self.balance - amount
            print(f"{amount} withdrawn")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Balance increased")

    def info(self):
        return self.balance

