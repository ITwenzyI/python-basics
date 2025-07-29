# Schlüssel-Wert Paare
# {}
# Schlüssel einzigartig

leeres_dict = {}

einkaufs_dict = {
    "Apfel": 1000,
    "Birne": 999,
    "Trauben": 777,
}
print(einkaufs_dict)
print(einkaufs_dict["Apfel"])
print(einkaufs_dict.keys())
print(einkaufs_dict.values())

# Wert verändern
einkaufs_dict["Apfel"] = 3

# Paare hinzufügen
einkaufs_dict["Neu"] = "Neuer"

# Paare entfernen
einkaufs_dict.pop("Birne")
print(einkaufs_dict)

for i in einkaufs_dict:
    print(i)
    print(einkaufs_dict[i])