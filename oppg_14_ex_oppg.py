import csv

filnavn = "eks_oppg.csv"

# Lister for å ta vare på alle årstall og befolkningsstørrelser
startlokasjoner = []

with open(filnavn, encoding="utf-8-sig") as fil:
  filinnhold = csv.reader(fil, delimiter=",")

  overskrifter = next(filinnhold)
  print(overskrifter)
  

  n = 0
  for rad in filinnhold:
      startlokasjoner.append(rad[])

#print(startlokasjoner)
antall = startlokasjoner.count("Schous plass")

