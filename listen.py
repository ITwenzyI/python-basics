#Leere List
leere_liste = []
print(leere_liste)

# List mit 2 Datatypen
double_liste = [12, "hallo", "3tes Element", 4] # 0,1,2,3,...
print(double_liste)
print(double_liste[1][1]) # 2 Element 2 Buchstabe
print(type(double_liste[0]))

# List anhängen
double_liste.append("Append-Element")
print(double_liste)

# List einfügen
double_liste.insert(0, "Insert-Element")
print(double_liste)

# List entfernen
double_liste.remove("hallo")
print(double_liste)

# List letztes Element entfernen
double_liste.pop()
print(double_liste)

# List an bestimmter Stelle löschen
del double_liste[0]
print(double_liste)

print("\nNeue List \n")
# Neue List
new_list = ["A", "B", "C", "D", "E", "F"]
print(len(new_list))
print(min(new_list))
print(max(new_list))
print(new_list[1:len(new_list)])

# List in List

list_list = ["abc", "efg", "fhg", ["yaz", "zaz"]]
print(list_list)
print(list_list[3][1][1:3]) # 4 Element 2 Position 2 Buchstabe
