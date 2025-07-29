# 1. Spielfeld erstellen
def erstellung_spielfeld():
    spielfeld = []

    for i in range(3):
        zeile = [" ", " ", " "]
        spielfeld.append(zeile)
    return spielfeld

# 2. Spielfeld ausgeben
def print_spielfeld(spielfeld):
    for zeile in spielfeld:
        print("|".join(zeile))
        print("------")


# Spiel starten
def play_game():
    brett = erstellung_spielfeld()
    aktueller_spieler = "X"

    while True:
        print_spielfeld(brett)
        zeile = int(input(f"Spieler {aktueller_spieler}, wähle deine Zeile (0-2): "))
        spalte = int(input(f"Spieler {aktueller_spieler}, wähle deine Spalte (0-2): "))
        if not zug(brett, aktueller_spieler, zeile, spalte)

# 3. Zug
def zug(spielfeld, spieler, zeile, spalte):
    if spielfeld[zeile][spalte] == " ":
        spielfeld[zeile][spalte] = spieler
        return True
    else:
        return False

play_game()