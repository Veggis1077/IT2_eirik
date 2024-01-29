import matplotlib.pyplot as plt

utdanningsprogram = [
  "Bygg- og anleggsteknikk",
  "Elektro og datateknologi",
  "Helse- og oppvekstfag",
  "Naturbruk",
  "Restaurant- og matfag",
  "Teknologi- og industrifag",
  "Håndverk, design og produktutvikling",
  "Frisør, blomster, interiør og eksponeringsdesign",
  "Informasjonsteknologi og medieproduksjon",
  "Salg, service og reiseliv"
]

antall = [3811, 4168, 8661, 2057, 1484, 5501, 313, 901, 1309, 2061]

plt.figure(figsize=(10, 5))  # Angir dimensjoner for figure-objektet

plt.barh(utdanningsprogram, antall)  # Lager stolpediagrammet

plt.subplots_adjust(left=0.4)  # Øker plassen på venstre side av diagrammet

plt.grid(axis="x")  # Legger til rutenett (bare vertikale linjer)
plt.show()
# Viser diagrammet