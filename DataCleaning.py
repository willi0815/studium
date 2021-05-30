# Aufgabe 6.1
# Jürgen Weidig

#from numpy import int16
import numpy as np
import pandas as pd
#df = pd.read_csv("C:/Users/Juergen/Google Drive/Studium/Data Science/Aufgabe 06/dsm-beuth-edl-demodata-dirty.csv")
df = pd.read_csv('https://raw.githubusercontent.com/edlich/eternalrepo/master/DS-WAHLFACH/dsm-beuth-edl-demodata-dirty.csv',)
print("Ausgabe Daten: *****************")
print(df)

print()
print("Anzeige der Datentypen: ********")
# Anzeige der Datentypen
print (df.dtypes)

print()
print("Spalten auf Leerzeichen untersuchen: ********")
fullname = df['full_name'].unique()
firstname = df['first_name'].unique()
lastname = df['last_name'].unique()
email = df['email'].unique()
print("fullname: " + np.array2string(fullname))
print()
print("first_name: " + np.array2string(firstname))
print()
print("last_name: " + np.array2string(lastname))
print()
print("email: " + np.array2string(email))

print()
print("Spalte age in Zahl wandeln: ****")
df.age = pd.to_numeric(df.age, errors='coerce')
print(df)

print()
print("Zeilen mit NaN entfernen: ********")
df_a = df.dropna()
print(df_a)

print()
print("Spalte id, age in Integer wandeln: ****")
# wird unterstellt das die Spalte id nicht benötigt wird um mit anderen Daten 
# verlinkt zu werden, dann kann diese gelöscht werden,
# sonst muss die Spalte bestehen bleiben, der Datentyp sollte auf Integer geändert werden

# alle Spalten sind Objects, d.h String ausser Spalte id
# Spalte id konvertieren von float64 nach int
print (df_a.dtypes)
df_a.loc[:, 'id'] = df_a.id.astype(int)
df_a.loc[:, 'age'] = df_a.age.astype(int)
print (df_a.dtypes)
print(df_a)

print()
print("Einträge die Alter < 10 entfernen: ****")
# wir entfernen nun alle datensätze die kleiner als 10 sind incl. negativer Einträge,
# da man nicht prüfen kann ob nur das Vorzeichen falsch ist oder die ganze Zahl
df_a.drop(df_a[df_a.age < 10].index, inplace = True)
print(df_a)

print()
print("Doppelte Zeilen entfernen: ****")
# doppelte Zeilen entfernen, Parameter mit allen Spaltennamen damit wirklich nur doppelte Einträge entfernt werden
df_c = df_a.drop_duplicates(subset=['full_name', 'first_name', 'last_name', 'email', 'gender', 'age'], keep='first')
print(df_c)
