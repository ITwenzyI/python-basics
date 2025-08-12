def debug_info(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

debug_info(1, 2, 3, "213",mode="fast", debug=True)

def f(a, b, /, c, *, d):
    print(a, b, c, d)

f(1, 2, c=3, d=4)
f(1, 2, 3, d=4)

def area_rectangle(width, height, /):
    return width * height

def introduce(name, age):
    print(f"Ich bin {name} und {age} Jahre alt")

introduce(age=25, name="Kilian")

def greet(name, greeting="Hallo"):
    print(f"Hi {name}, welcome {greeting}")
greet(name="Kilian")
def greet(name, greeting=None):
    if greeting is None:
        greeting = ["Hallo"]
    print(f"Hi {name}, welcome {greeting}")
greet(name="Kilian")

def multiply_all(*args):
    result = 1
    for arg in args:
        result *= arg
    print(result)
    return result
multiply_all(1, 2, 3)
multiply_all(*[2, 5, 0])
multiply_all()
# args ist eine Tuple

def print_settings(**kwargs):
    print(kwargs)
print_settings(color="blue", font=14)
print_settings(font=10, **{"fontt": 12})
# kwargs ist ein Dictionary

def debug_info(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)
debug_info(1, x=2, *[3, 4], **{"y": 5})

def calc(a, b, /, c, *, d):
    print((a + b + c) * d)
calc(1, 2, c=3, d=4)
#calc(a=1, b=2, c=3, d=4)