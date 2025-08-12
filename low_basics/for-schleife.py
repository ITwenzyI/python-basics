liste = ["Apfel", "Birne", "Traube"]

for i in liste:
    print(i)

new_list = [1500, 1000, 500, 3000, 10000, 200]
bezahlbar = []

for i in new_list:
    if i <= 1500:
        bezahlbar.append(i)
    else:
        print(i, "Nicht Bezahlbar")

print(bezahlbar)