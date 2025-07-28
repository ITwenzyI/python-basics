
# String Indexing
berufsfeld = "IT"
print("Ich habe schon Erfahrung im Bereich " + berufsfeld)
print(berufsfeld[-1]) # print(berufsfeld[0])

# String Slicing
x = "abcdefg hijk"
print(x[:9]) # print(x[1:9])

# String Länge
y = "Wie lange bin ich?"
print(len(y))

# String Teile verändern
g = "hallo"
g = "H" + g[1:]
print(g)

# String Multiplizieren
q = "Hallo"
zahl = 100
print(q * 10)
print(q + str(zahl))

# Upper / Lower
z = "Upper"
print(z.upper())
u = "LOwER"
print(u.lower())

# Split
spliter = "Hallo Welt, ich lerne, Python gerade"
print(spliter.split(", "))

# Find
finder = "Ich liebe Python gerade :)"
print(finder.find("Python"))