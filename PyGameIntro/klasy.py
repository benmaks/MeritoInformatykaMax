from math import sqrt, pow

# 1
class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        print(f"{self.imie} {self.nazwisko}, {self.wiek}")

osoba1=Osoba("Piotr", "Kowalski", "31")
osoba2=Osoba("Anna", "Nowak", "34")

osoba1.przedstaw_sie()
osoba2.przedstaw_sie()


# 2
class Kwadrat:
    def __init__(self, bok):
        self.bok = bok

    def obwod(self):
        return 4*self.bok

    def pole(self):
        return self.bok*self.bok

kwadrat1 = Kwadrat(8)

print(f"Obwód: {kwadrat1.obwod()}")
print(f"Pole: {kwadrat1.pole()}")


# 3
class Student(Osoba):
    def __init__(self, imie, nazwisko, wiek, oceny):
        super().__init__(imie, nazwisko, wiek)
        self.oceny = oceny

    def srednia(self):
        lista_ocen = self.oceny
        lista_ocen = lista_ocen.split(",")
        lista_ocen = list(map(int, lista_ocen))
        return sum(lista_ocen)/len(lista_ocen)

student1 = Student("Eugieniusz", "Stasiak", "22", "3,4,5,3,2,4,5,4,5,4,3,2")

print(f"Średnia: {student1.srednia()}")


# 4
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def odleglosc(self, punkt2):
        return (sqrt(pow(punkt2.x-self.x, 2) + pow(punkt2.y - self.y, 2)))

punkt1 = Punkt(6, 9)
punkt2 = Punkt(3, 14)

print(punkt1.odleglosc(punkt2))


# 5
class Samochod:
    def __init__(self, marka, model, kolor, predkosc):
        self.marka = marka
        self.model = model
        self.kolor = kolor
        self.predkosc = predkosc

    def przyspiesz(self, wartosc):
        self.predkosc += wartosc

    def zwalnij(self, wartosc):
        self.predkosc -= wartosc

samochod1 = Samochod("Fiat", "126p", "czerwony", 50)

samochod1.przyspiesz(5)
samochod1.zwalnij(10)

print(samochod1.predkosc)

# 6
class KontoBankowe:
    def __init__(self, saldo):
        self.saldo = saldo

    def wplac(self, wartosc):
        self.saldo += wartosc

    def wyplac(self, wartosc):
        self.saldo -= wartosc

konto_bankowe1 = KontoBankowe(420)

konto_bankowe1.wplac(52)
konto_bankowe1.wyplac(16)

print(konto_bankowe1.saldo)

# 7
class Zegar:
    def __init__(self):
        self.godzina = 0
        self.minuta = 0
        self.sekunda = 0

    def ustaw_czas(self, godzina, minuta, sekunda):
        self.godzina = godzina
        self.minuta = minuta
        self.sekunda = sekunda

    def odliczaj(self):
        self.sekunda -= 1
        if self.sekunda <= -1:
            self.minuta -= 1
            self.sekunda = 59
        if self.minuta <= -1:
            self.godzina -= 1
            self.minuta = 59
        if self.godzina <= -1:
            self.godzina = 23
            self.minuta = 60
            self.sekunda = 59

zegar1 = Zegar()

zegar1.ustaw_czas(21, 37, 42)
zegar1.odliczaj()

print(f"{zegar1.godzina}:{zegar1.minuta}:{zegar1.sekunda}")


# 8
class Ksiazka:
    def __init__(self, tytul, autor, strony):
        self.tytul = tytul
        self.autor = autor
        self.strony = strony

    def opis(self):
        print(self.tytul + " - " + self.autor + ", " + self.strony)

ksiazka1 = Ksiazka("Przemiana", "Franz Kafka", str(146))

ksiazka1.opis()


# 9
class Prostokat:
    def __init__(self, dlugosc, szerokosc):
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def czy_kwadrat(self):
        return self.dlugosc == self.szerokosc


prostokat1 = Prostokat(3, 3)

print(prostokat1.czy_kwadrat())


# 10
class Kalkulator:
    def __init__(self, wynik):
        self.wynik = wynik

    def dodaj(self, dodaj):
        self.wynik += dodaj
        return self.wynik

    def odejmij(self, odejmij):
        self.wynik -= odejmij
        return self.wynik

    def pomnoz(self, pomnoz):
        self.wynik *= pomnoz
        return self.wynik

    def podziel(self, podziel):
        self.wynik /= podziel
        return self.wynik

kalkulator1 = Kalkulator(0)

kalkulator1.dodaj(1)
kalkulator1.odejmij(2)
kalkulator1.pomnoz(3)
kalkulator1.podziel(4)
print(kalkulator1.wynik)