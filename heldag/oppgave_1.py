import csv

class Fil:
    def __init__(self, filnavn, deli=";"):
        self.deli = deli
        self.filnavn = filnavn
        self.filtype = self.filnavn.split(".")[-1]
        self.dic = {}
        self.liste = []
        self.filinnhold = ""
        self.etternavn = []
        self.sorterer = []

    def csv(self):
        with open(self.filnavn, encoding="utf-8-sig") as fil:
            self.filinnhold = csv.reader(fil, delimiter=";")
            eks_liste = []
            for i in self.filinnhold:
                eks_liste.append(i)
            finliste = []

            for i in range(len(eks_liste)):
                x = eks_liste[i][0].split(",")
                a = x[0].split(" ")[1]
                self.etternavn.append(a)
                self.dic[a] = [x[0], x[1], x[2]]
                self.sorterer.append([a, x[0], x[1], x[2]])
                finliste.append(x)
            self.liste = []  # liste uten duplikater
            for j in (finliste):
                if j not in self.liste:
                    self.liste.append(j)

    def sok(self):
        postnr = input("Hvilket postnummer vil du søke etter >>>")
        for i in self.liste:
            if postnr == i[2]:
                print([i[0], i[1]])
    def sorter(self):
        a = sorted(self.sorterer)
        for i in a :
            print(i[1], i[2], i[3])
    def lengde(self):
        print(f"Det er {len(self.sorterer)} personer registrert i adresselisten")

class Txtfil(Fil):
    def __init__(self, filnavn, lstcsv=[]):
        self.lstcsv = lstcsv
        super().__init__(filnavn)
    def text(self):
        self.liste = []
        with open(self.filnavn, encoding="utf-8-sig") as f:
            for i in f:
                self.liste.append(i)
        for i in range(len(self.liste)):
            self.liste[i] = (self.liste[i][:-1])
        full = []
        hel = []
        for i in self.liste:
            if i == "":
                hel.append(full)
                full = []
            else:
                full.append(i)
        self.liste = hel
        for i in range(len(self.liste)):
            x = self.liste[i]
            a = x[0].split(" ")[1]
            self.etternavn.append(a)
            self.dic[a] = [x[0], x[1], x[2]]
            self.sorterer.append([a, x[0], x[1], x[2]])

    def fjernlike(self,a, b):
        for i in a[:]:
            if i in b:
                a.remove(i)
                b.remove(i)
        print(len(a), len(b))

csv_fil = Fil("adresser.csv", ",") # Oprpretter klasse med csv filen
csv_fil.csv()#Får filen organisert
txt_fil = Txtfil("adresser-kopi.txt", csv_fil.sorterer) #Oppretter klassen som har arvet fra fil klassen med txt filen
txt_fil.text() #Gjjør filen fin ( likt som Fil.csv()
txt_fil.lengde()#Finner lengde før jeg har fjernet elementer fra listene
txt_fil.sorter()#Sorterer txt filen i alfabetisk rekkefølge
csv_fil.sorter() #Sorterer csv filen i alfabetisk rekkefølge
csv_fil.sok()#Søker etter adresser gitt et postnr
txt_fil.sok()#Søker eter adrese og navn gitt postnr på txt filen
txt_fil.fjernlike(txt_fil.sorterer, csv_fil.sorterer) #Fjerner like elementer fra begge listene
txt_fil.lengde() #Lengde etter fjernet
csv_fil.lengde()