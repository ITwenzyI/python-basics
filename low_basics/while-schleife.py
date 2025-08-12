counter = 0


while counter <= 5:
    print(counter)
    counter += 1

einkaufslist = []
#
# while decision == "yes":
#     einkaufslist.append(input("Was möchtest du deiner Liste hinzufügen? : "))
#     decision = input("Would you like to continue? (yes/no): ")
#
# print(einkaufslist)

# Artikel hinzufügen
# Aktion -> hinzufügen, entfernen, anzeigen, beenden

while True:
    action = input("1. Hinzufügen\n"
                   "2. Entfernen\n"
                   "3. Anzeigen\n"
                   "4. Beenden\n"
                   " Enter your choice: ")

    if action == "1":
        eingabe = input("Was möchtest du hinzufügen: ")
        einkaufslist.append(eingabe)

    elif action == "2":
        eingabe = input("Was möchtest du entfernen: ")
        if eingabe not in einkaufslist:
            print("Nicht auf der Einkaufsliste!")
        else:
            einkaufslist.remove(eingabe)

    elif action == "3":
        print(einkaufslist)

    elif action == "4":
        break

    else:
        print("Invalid choice!")