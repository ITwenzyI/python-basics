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

# 3. Zug
def zug(spielfeld, spieler, zeile, spalte):
    if spielfeld[zeile][spalte] == " ":
        spielfeld[zeile][spalte] = spieler
        return True
    else:
        return False

# 4. Result
def result(spielfeld, spieler):
    for zeile in range(3):
        if spielfeld[zeile][0] == spielfeld[zeile][1] == spielfeld[zeile][2] == spieler:
            return True

    for spalte in range(3):
        if spielfeld[0][spalte] == spielfeld[1][spalte] == spielfeld[2][spalte] == spieler:
            return True

    if spielfeld[0][0] == spielfeld[1][1] == spielfeld[2][2] == spieler or \
        spielfeld[0][2] == spielfeld[1][1] == spielfeld[2][0] == spieler:
        return True

# 5. Unentschieden
def unentschieden(brett):
    for zeile in brett:
        if " " in zeile:
            return False
    return True


# Spiel starten
def play_game():
    brett = erstellung_spielfeld()
    aktueller_spieler = "X"

    while True:
        print_spielfeld(brett)

        try:
            zeile = int(input(f"Spieler {aktueller_spieler}, wähle deine Zeile (0-2): "))
            spalte = int(input(f"Spieler {aktueller_spieler}, wähle deine Spalte (0-2): "))
            if zeile < 0 or zeile > 2 or spalte < 0 or spalte > 2:
                print("Außerhalb des Spielfelds!")
            else:
                if not zug(brett, aktueller_spieler, zeile, spalte):
                    print("Invalid! Try again.")
        except ValueError:
            print("Ganzzahl!")


        if result(brett, aktueller_spieler):
            print_spielfeld(brett)
            print(f"Du hast gewonnen Spieler {aktueller_spieler}")
            break
        elif unentschieden(brett):
            print_spielfeld(brett)
            print("Unentschieden!")
            break

        aktueller_spieler = "O" if aktueller_spieler == "X" else "X"

play_game()