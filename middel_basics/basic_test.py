#1
from random import randint


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

#2
list_1 = [i**2 for i in range(11)]
print(list_1)

#3
text = "Python ist toll"
#a
print(text[0], text[-1])
#b
print(text[::-1])

#4
for i in range(21):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")

#5
nums = [4, 7, 2, 9, 12, 15]
even_nums = []
for num in nums:
    if is_even(num):
        even_nums.append(num)
print(even_nums)

#6
# random_number = randint(1, 100)
# while True:
#     user_input = int(input("Enter a number: "))
#     if user_input == random_number:
#         print("Correct!")
#         break
#     elif user_input > random_number:
#         print("Zu groß!")
#     else:
#         print("Zu Klein!")

#7
def multiply_all(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

#8
def format_person(*, name, age):
    return {'name': name, 'age': age}

#9
def safe_div(a, b):
    if b == 0:
        return None, "Division by zero"
    else:
        result = a / b
        return result, None

#10
fruits = ["Apfel", "Banane", "Kirsche", "Apfel", "Banane"]
print(set(fruits))
#b
dict = {}
for fruit in fruits:
    if fruit in dict:
        dict[fruit] = dict[fruit] + 1
    else:
        dict[fruit] = 1
print(dict)

#11
people = [
    {"name": "Anna", "age": 25},
    {"name": "Ben", "age": 30}
]
for person in people:
    person["age"] += 1
    print(person)

#12
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line)

#13
import json

with open("settings.json", "r", encoding="utf-8") as f:
    data = json.load(f)

data["theme"] = "dark"

with open("settings.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)



