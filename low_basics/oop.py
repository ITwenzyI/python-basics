class Auto():
    """"
    Das ist die Klasse Auto(Meine erste Klasse in Python)
    """
    def __init__(self, marke, modell, baujahr, doors):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
        self.wheels = 4
        self.doors = doors

    def print(self):
        print(self.marke, self.modell, self.baujahr, self.wheels, self.doors)

    def startup(self):
        print("Welcome! Auto is starting up...")

class Porsche(Auto):
    """"
    Das ist die Klasse Porsche. Sie erbt von Auto
    """
    def __init__(self, marke, modell, baujahr, doors, ps, price):
        super().__init__(marke, modell, baujahr, doors)
        self.ps = ps
        self.price = price

    def print(self):
        print(self.marke, self.modell, self.baujahr, self.doors, self.ps, self.price)

auto1 = Auto("BMW", "M320", "2020", 4)
auto1.print()

porsche1 = Porsche("Porsche", "Panamera Turbo S", "2021", 4, 500, 200.000)
porsche1.print()