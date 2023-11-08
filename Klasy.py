import math

class MojaKlasa:
    zmienna = 'blah'

    def funkcja(self):
        print("To jest wiadomość wewnątrz klasy")


class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def przedstaw_sie(self):
        print(f"Cześć, jestem {self.imie} i mam {self.wiek} lat")


osoba1 = Osoba("Anna", 25)

osoba2 = Osoba("Tomasz", 30)

osoba1.przedstaw_sie()
osoba2.przedstaw_sie()


class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def odleglosc_od_zera(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

punkt1 = Punkt(3, 4)
punkt2 = Punkt(-5, -12)

print(f"Ten punkt jest oddalony o {punkt1.odleglosc_od_zera()} jednostek od zera.")
print(f"Ten punkt jest oddalony o {punkt2.odleglosc_od_zera()} jednostek od zera.")