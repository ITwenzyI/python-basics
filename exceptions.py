try:
    ergebnis = 10 / 2
except ZeroDivisionError:
    print("Fehler! Division durch 0!")
except TypeError:
    print("Fehler! Keine Kompatieblen Typen!")
except: # Allgemeiner Fehler ( Alles )
    print("Fehler! Fehler!")
# else:
#     print("Top passt alles")
finally:
    print("Alles ist durchgelaufen!")

# Exceptions Raisen
x = 10
if x >= 10:
    raise Exception("Sorry! X darf nicht = oder > 10 sein!")