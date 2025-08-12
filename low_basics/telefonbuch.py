telefonbuch = {
    "Polizei": "110",
    "Krankenwagen": "112",
    "Feuerwehr": "112",
    "FBI": "999"
}
eingabe = input("Welche Telefonnummer? : ")
if eingabe in telefonbuch:
    print(eingabe, ": ", telefonbuch[eingabe])
else:
    print("Fehler!")
#print("Polizei: ", telefonbuch["Polizei"])
del telefonbuch[eingabe]
print(eingabe, " wurde entfernt!")