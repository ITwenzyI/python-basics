wahr = True # 1
falsch = False # 0

print(type(wahr))
print(2 > 1)
print(2 < 1)
print(2 >= 2)
print(2 == 1)
print(2 < 1 or 1 < 2)
print(2 < 1 and 3 < 2)

strecke_km = int(input("Strecke in KM: "))

if strecke_km < 3:
    print("Kurze Strecke! Empfehlung zu Fuß!")
elif 3 <= strecke_km < 7:
    print("Mittlere Strecke! Empfehlung mit Fahrrad!")
else:
    print("Lange Strecke! Empfehlung mit Auto!")

tickettyp = int(input("Welcome to the Ticket System. What is your age? : "))
anzahl = int(input("How many tickets : "))

if tickettyp <= 0:
    print("Error! Invalid Age!")
elif tickettyp < 18:
    print("That would be", anzahl*5, " Euro for the Tickets!")
elif tickettyp < 65:
    print("That would be", anzahl*10, "Euro for the Tickets!")
elif tickettyp < 100:
    print("That would be", anzahl*7.5, "Euro for the Tickets!")
else:
    print("Error! Invalid Age!")
