# Zahlenraten
# Jürgen Weidig
leseEingabe <- function()
{ 
  n <- readline(prompt= paste("Eingabe deiner Zahl zwischen ",untereGrenze," bis ",obereGrenze , ": "))
  if(!grepl("^[0-9]+$",n))
  {
    print(paste(n," ist die falsche Eingabe."))
    return(leseEingabe())
  }
  return(as.integer(n))
}
untereGrenze <- 0
obereGrenze <- 100
versuchsZaehler <- 0
zufallsZahl <- round(runif(1, untereGrenze,obereGrenze),0)
print("Raten einer Zufallszahl")
eingabeNutzer <- -1
#print(zufallsZahl)
#print(eingabeNutzer)
while(zufallsZahl != eingabeNutzer)
{ 
  eingabeNutzer <- leseEingabe()
  versuchsZaehler <- versuchsZaehler + 1
  #print(zufallsZahl)
  #print(eingabeNutzer)
  if (eingabeNutzer == zufallsZahl)
  {
    print(paste("Sie haben ", versuchsZaehler, " Versuche benötigt."))
    print("Gewonnen. Das war die Zahl.")
  }
  if (eingabeNutzer > zufallsZahl)
  {
    print("Die Zahl ist zu groß.")
  }
  if (eingabeNutzer < zufallsZahl)
  {
    print("Die Zahl ist zu klein.")
  }
  if (eingabeNutzer > obereGrenze)
  {
    print(paste(eingabeNutzer," liegt ausserhalb des Bereiches."))
  }
}
print("Spiel beendet.")