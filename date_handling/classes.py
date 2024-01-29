import pandas as pd
from pathlib import Path
class Fil:
    def __init__(self, filnavn, deli=";"):
        self.deli = deli
        self.fil = Path(__file__).parent.parent / filnavn
        self.df = pd.read_csv(self.fil, delimiter=deli)
        self.dict = {}
        for i in self.df:
            print(i)
        for i in self.df:
            self.dict[i[1]] = i[2]


a = Fil("fjernsyntid.csv")
print(a.dict)
