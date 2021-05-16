spielAktiv = True
aktuellerSpieler = 'O'
feld = ["0","1","2","3","4","5","6","7","8"]

def spielfeldAnzeigen():
    print (feld[0] + "|" + feld[1] + "|" + feld[2] )
    print ("-----" )
    print (feld[3] + "|" + feld[4] + "|" + feld[5] )
    print ("-----" )
    print (feld[6] + "|" + feld[7] + "|" + feld[8] )

def eingabeSpieler():
    global spielAktiv
    while True:
        spielzug = input("Bitte Feld eingeben, 'e' für Ende: ")
        if spielzug == 'E' or spielzug == 'e':
            beenden("")
            return
        try:
            spielzug = int(spielzug)
        except ValueError:
            print("Bitte Zahl von 0 bis 8 eingeben.")
        else:
            if spielzug >= 0 and spielzug <= 8:
                if feld[spielzug] == 'O' or feld[spielzug] == 'X':
                    print("Das Feld ist belegt, bitte neu wählen.")
                else: 
                    return spielzug
            else:
                print("Zahl muss zwischen 0 und 8 liegen.")

def pruefungGewonnen():
     # Spalte
    if feld[0] == feld[3] == feld[6]: return feld[0]
    if feld[1] == feld[4] == feld[7]: return feld[1]
    if feld[2] == feld[5] == feld[8]: return feld[2]
    # Diagonale
    if feld[0] == feld[4] == feld[8]: return feld[4]
    if feld[6] == feld[4] == feld[2]: return feld[4]
    # Reihe
    if feld[0] == feld[1] == feld[2]: return feld[0]
    if feld[3] == feld[4] == feld[5]: return feld[3]
    if feld[6] == feld[7] == feld[8]: return feld[6]

def pruefungUnentschieden():
    if (feld[0] == 'X' or feld[0] == 'O') and (feld[1] == 'X' or feld[1] == 'O') \
      and (feld[2] == 'X' or feld[2] == 'O') and (feld[3] == 'X' or feld[3] == 'O') \
      and (feld[4] == 'X' or feld[4] == 'O') and (feld[5] == 'X' or feld[5] == 'O') \
      and (feld[6] == 'X' or feld[6] == 'O') and (feld[7] == 'X' or feld[7] == 'O') \
      and (feld[8] == 'X' or feld[8] == 'O'): return ('unentschieden')

def beenden(meldung):
    print(meldung)
    print("Programm beendet.")
    spielAktiv = False
    return

spielfeldAnzeigen()
while spielAktiv:
    print()
    print ("Spieler " + aktuellerSpieler + " am Zug.")
    spielzug = eingabeSpieler()
    if isinstance(spielzug, int):
        if spielzug >=0 and spielzug <=8:
            feld[spielzug] = aktuellerSpieler
            spielfeldAnzeigen()
            gewonnen = pruefungGewonnen()
            if gewonnen:
                beenden("Spieler " + gewonnen + " hat gewonnen!")
                break
            if pruefungUnentschieden():
                beenden("Spiel ist unentschieden ausgegangen.")
            if aktuellerSpieler == 'X': aktuellerSpieler = 'O'
            else: aktuellerSpieler = 'X'
print()