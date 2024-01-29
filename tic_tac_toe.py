brett = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
print([" " for x in range(2)])
for i in range(9):
    print(brett)
    if i%2 ==0:
        kar = "x"
    else:
        kar = "o"
    plass = list(input("Skriv inn posisjon på form: x, y"))
    brett[int(plass[0])][int(plass[-1])] = kar
    for j in range(3):
        a = [kar for x in range(3)]
        if brett[j][:] == a or brett[:][j] == a:
            print("spiller "+ kar+" vant")

