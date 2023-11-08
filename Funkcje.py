import string

# 1
def kwadrat(liczba):
    liczba = int(liczba)
    return liczba*liczba

# 2
def polacz_napisy(text1, text2):
    return text1 + " " + text2

# 3
def najw_w_lisc(lista):
    return max()
# 4
def srednia(lista):
    return sum(lista) / len(lista)

# 5
def dzielniki(liczba):
    dzielnik = [x for x in range(1, liczba) if liczba%x == 0]
    return dzielnik

# 6
def liczba_pierwsza(liczba):
    for i in range(2, liczba-1):
        if liczba % i == 0:
            return False
    return True

# 7
def fibonacci(liczba):
    a, b = 1, 1
    for i in range(liczba - 1):
        b += a
        a = b - a
    return a

# 8
def samogloski(tekst):
    lista = [x for x in tekst if x in ["a", "e", "i", "o", "u", "y"]]
    return len(lista)

# 9
def odwroc_tekst(tekst):
    return tekst[::-1]

# 10
def panagram(zdanie, alphabet=string.ascii_lowercase):
    return set(alphabet) <= set(zdanie.lower())

