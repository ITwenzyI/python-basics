import zahlen


def begruessung(name):
    print("Hallo", name)

begruessung("Kilian")

def addition(a, b):
    print(a + b)
    return a + b
def subtraction(a, b):
    print(a - b)
    return a - b
def multiplication(a, b):
    print(a * b)
    return a * b
def division(a, b):
    print(a / b)
    return a / b
def add(a = 2, b=4):
    print(a + b)
    return a + b

addition(4, 5)
add()

def hallo(name, alter):
    print(name, alter)
hallo(alter = 32, name = "Kilian")


# Konkrete Zuweisung mehrerer Daten
def addieren(*zahlen):
    print(sum(zahlen))
addieren(1, 2, 3, 4)

# Defininieren mit Dictionarie
def addieren2(**daten):
    print(daten)
addieren2(name= "Kilian", alter= 32, hobby = "python")

# Später Definieren
def nichtfertig():
    pass
