class Mangekant:
    def __init__(self, asider):
        self.asider = asider
        self.lengde = []
        self.sum = 0
    def skrivinn(self):
        for i in range(self.asider):
            self.lengde.append(float(input(f"lende side{i}")))

    def omkrets(self):
        for i in self.lengde:
            self.sum+=i
        return self.sum
    def __str__(self):
        return f"antall sider>{self.asider} lengde på siderne>{self.lengde}, omkrets {self.sum}"

trekant = Mangekant(3)
trekant.skrivinn()
trekant.omkrets()
print(trekant)
