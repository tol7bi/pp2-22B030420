import math
import random
from itertools import permutations



def ounces(grams):
    print(28.3495231 * grams)


def temperature(f):
    c = (5/9) * (f-32)
    print(c)


def puzzle(numheads, numlegs):
    c = 2*numheads - 0.5*numlegs
    r = numheads - 2 * numheads + 0.5*numlegs

    print(f" rabbits - {int(r)}, chicken - {int(c)}")

def prime(n):
    flag = True
    if n == 0 or n == 1:
        return False
    i = 2
    while i <= n/2:
        if n % i == 0:
            flag = False
            break
        i += 1
    return flag


def filter_prime(numbers:list):
    prime_numbers = []
    for i in numbers:
        if prime(i):
            prime_numbers.append(i)
    print(prime_numbers)


def perm(s):
    for i in list(permutations(list(s))):
        print(i)


def reverse(s:str):
    words = s.split(sep=" ")
    print(" ".join(words[::-1]))


def has33(nums):
    s = ''.join([str(x) for x in nums])
    if "33" in s:
        return True
    else:
        return False


def spy_game(nums):
    s = ''.join([str(x) for x in nums if x == 7 or x == 0])
    if "007" in s:
        return True
    else:
        return False




def volume(radius):
    v = 4/3 * math.pi * radius**3
    return v


def uniq(nums:list):
    uni = []
    for i in nums:
        if i not in uni:
            uni.append(i)
    return uni


def palindrome(x):
    return str(x) == str(x)[::-1]


def histogram(l:list):
    for i in l:
        print("*" * i)


def guess():
    name = input("Hello! What is your name?\n")
    num = random.randint(1, 20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    answer = int(input("Take a guess.\n"))
    count = 0
    while True:
        count = count + 1
        if answer > num:
            print("Your guess is too high")
        elif answer < num:
            print("Your guess is too low")
        elif answer == num:
            print(f"You are right! Number of guesses is {count}")
            break
        answer = int(input("Take a guess\n"))


guess()
