# Aufgabe 4.3
# Jürgen Weidig

import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/edlich/eternalrepo/master/DS-WAHLFACH/countries.csv")
print("Informationen: *****************")
print(df)
print(df.describe())

print("Letzten 4 Zeilen: *****************")
print(df[-4:])

print("Show all the row of countries who have the EURO: ")
result = df[df['Currency']=='EUR']
print(result)

#-	Show only name and Currency in a new data frame
print("Show only name and Currency in a new data frame: ")
result = df[["Name", "Currency"]] #age_sex = titanic[["Age", "Sex"]]
print(result)

print("Show only the rows/countries that have more than 2000 BIP: ")
result = df[df['BIP']>2000]
print(result)

print("Select all countries where with inhabitants between 50 and 150 Mio: ")
result = df.loc[(df['People'] > 50000000) & (df['People'] < 150000000)]
print(result)

print("Change BIP to Bip: ")
result = df.rename(columns={"BIP": "Bip"}, errors="raise")
print(result)

print("Calculate the Bip sum: (Summenzeile hinzugefügt) ")
result = result.append(result.sum(numeric_only=True), ignore_index=True)
print(result)

print("Calculate the average people of all countries: ")
print(df["People"].mean())

print("Sort by name alphabetically: ")
result = df.sort_values(by='Name')
print(result)

# all countries with > 1000000 get BIG and <= 1000000 get SMALL in the cell replaced
print("Create a new data frame from the original where the area is changed.. : ")
result = pd.DataFrame(df)
result['Area'].where(~(result.Area > 1000000), other='BIG', inplace=True)
result['Area'].where(~(result.Area != 'BIG'), other='SMALL', inplace=True)
print(result)