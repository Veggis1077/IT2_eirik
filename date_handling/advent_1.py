liste = []
with open("textfil-kopi.txt") as f:
    for i in f:
        liste.append(i)
for i in range(len(liste)):
    liste[i] = (liste[i][:-1])
maxsum = 0
a = 0
nyliste = []
for i in liste:
    if i == "":
        nyliste.append(a)
        if maxsum < a:
            maxsum = a
            a = 0
        else:
            a = 0
    else:
        a+=int(i)
nyliste.sort()
print(maxsum)
print(maxsum + nyliste[-2] + nyliste[-3])