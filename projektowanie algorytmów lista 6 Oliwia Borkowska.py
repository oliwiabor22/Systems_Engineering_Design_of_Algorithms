# Oliwia Borkowska projektowanie algorytmów lista 6 - algorytmy teorioliczbowe i RSA

# zadanie 1. Zaimplementuj funkcję, która zwróci listę czynników pierwszych zadanej liczby naturalnej n. Zrób to reku-
# rencyjnie, sprawdzając podzielność liczby przez kolejne liczby naturalne (aż do ⌊√n⌋) – rekurencja pojawia
# się, gdy liczba jest podzielna – wtedy uruchamiamy algorytm na jej dzielnikach.
# Wejście: liczba naturalna n.
# Wyjście: lista dzielników liczby n
print("Zadanie 1")
import math

def rozklad_na_czynniki_pierwsze(n):
    def rozklad(n, d=2):
        if n < 2:
            return []
        while d <= math.isqrt(n):
            if n % d == 0:
                return rozklad(d) + rozklad(n // d)
            d += 1
        return [n]
    return rozklad(n)

if __name__ == "__main__":
    try:
        n = int(input("Wprowadź liczbę naturalną: "))
        if n < 1:
            print("Liczba musi być naturalna (czyli całkowita większa od 0).")
        else:
            czynniki = rozklad_na_czynniki_pierwsze(n)
            print(f"Czynniki pierwsze liczby {n}: {czynniki}")
    except ValueError:
        print("Błąd! Wprowadź liczbę naturalną.")

# Zadanie nr 2– sito Eratostenesa
#  Zaimplementuj sito Eratostenesa, aby wyznaczyć zbiór liczb pierwszych nie większych od zadanego p
print("Zadanie 2")

def sito_eratostenesa(p):
    if p < 2:
        return []

    x = [0, 0] + [1] * (p - 1)

    for n in range(2, int(math.isqrt(p)) + 1):
        if x[n] == 1:
            for j in range(2, p // n + 1):
                x[n * j] = 0

    liczby_pierwsze = [i for i, is_prime in enumerate(x) if is_prime == 1]
    return liczby_pierwsze

if __name__ == "__main__":
    try:
        p = int(input("Wprowadź liczbę naturalną p, większą od 1: "))
        if p <= 1:
            print("Liczba musi być większa niż 1.")
        else:
            wynik = sito_eratostenesa(p)
            print(f"Liczby pierwsze ≤ {p}: {wynik}")
    except ValueError:
        print("Błąd! Wprowadź liczbę naturalną.")

#  Zadanie nr 3– największy wspólny dzielnik
#  3.1 Wyszukiwanie
#  Zaimplementuj funkcję szukającą największego wspólnego dzielnika dwóch liczb. Zrób to na dwa sposoby.
#  • Z wykorzystaniem rozkładu na czynniki pierwsze RNWD(a,b).
#  • Z wykorzystaniem algorytmu Euklidesa ENWD(a,b).
#  Wejście: dwie liczby a,b.
#  Wyjście: NWD(a,b) uzyskane na dwa sposoby.
#  1
# 3.2 Testy wydajności
#  Przygotuj procedurę testową do sprawdzenia czasu działania obu algorytmów.
#  Uruchamiaj RNWD(n,q) i ENWD(n,q) dla zadanej liczby n i dla kolejnych liczb naturalnych q do pewnego
#  zadanego m. Czasy działania obu algorytmów wyświetl na jednym wykresie.
#  Wejście: dwie liczby n,m.
#  Wyjście: wykres czasu działania dwóch algorytmów.
print("Zadanie 3.1")

def rozklad_na_czynniki(n):
    czynniki = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            czynniki.append(d)
            n //= d
        d += 1
    if n > 1:
        czynniki.append(n)
    return czynniki

# z wykorzytaniem rozkładu na czynniki pierwsze
def rnwd(a, b):
    cz_a = rozklad_na_czynniki(a)
    cz_b = rozklad_na_czynniki(b)

    wspolne = []
    for x in cz_a:
        if x in cz_b:
            wspolne.append(x)
            cz_b.remove(x)
    nwd = 1
    for w in wspolne:
        nwd *= w
    return nwd

# z wykorzystaniem algorytmu euklidesa
def enwd(a, b):
    while b != 0: # kiedy b nie jest równe 0
        a, b = b, a % b
    return a
if __name__ == "__main__":
    try:
        a = int(input("Wprowadź liczbę a: "))
        b = int(input("Wprowadź liczbę b: "))
        print(f"NWD({a}, {b}) z wykorzytsaniem rozkładu: {rnwd(a, b)}")
        print(f"NWD({a}, {b}) z wykorzytsaniem algorytmu Euklidesa: {enwd(a, b)}")
    except ValueError:
        print("Bład! Wprowadź liczby naturalne.")

print("Zadanie 3.2)")
import time
import matplotlib.pyplot as plt

def test_czasów(n, m):
    czasy_rnwd = []
    czasy_enwd = []
    qs = list(range(1, m + 1))

    for q in qs: # dla rwd
        start = time.perf_counter()
        rnwd(n, q)
        end = time.perf_counter()
        czasy_rnwd.append(end - start)

        start = time.perf_counter() # dla ewd
        enwd(n, q)
        end = time.perf_counter()
        czasy_enwd.append(end - start)

    plt.figure(figsize=(10, 5))
    plt.plot(qs, czasy_rnwd, label='RNWD (rozkład na czynniki)', color='magenta')
    plt.plot(qs, czasy_enwd, label='ENWD (algorytm Euklides)', color='blue')
    plt.xlabel('q')
    plt.ylabel('Czas w [s]')
    plt.title(f'Czas działania RNWD i czas działania ENWD dla n = {n}')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    try:
        n = int(input("Wprowadź liczbę n: "))
        m = int(input("Wprowadź maksymalną wartość q (m): "))
        test_czasów(n, m)
    except ValueError:
        print("Bład! Wprowadź liczby naturalne.")

# Zadanie nr 4– probabilistyczne testy piewszości
#  Zaimplementuj dwa algorytmy testowania pierwszości liczb
#  • test Fermata,
#  • test Millera-Rabina.
#  Wykorzystaj szybki algorytm potęgowania modulo.
#  Wejście: liczba potencjalnie pierwsza p.
#  Wyjście: rezultat testu pierwszości ww. algorytmami

print("Zadanie 4")
import random

# szybie potęgowanie modulo:
def szybkie_potegowanie(a, d, n):
    wynik = 1
    a = a % n
    while d > 0:
        if d % 2 == 1:
            wynik = (wynik * a) % n
        a = (a * a) % n
        d //= 2
    return wynik

# test fermata
def test_fermata(p, k=5):  # k = liczba prób
    if p <= 3:
        return p == 2 or p == 3
    if p % 2 == 0:
        return False

    for _ in range(k):
        a = random.randint(2, p - 2)
        if szybkie_potegowanie(a, p - 1, p) != 1:
            return False  # liczba na pewno jest złożona
    return True  # liczba jest prawdopodobnie pierwsza (ale nie na pewno)

# test millera-rabina
def test_miller_rabin(p, k=5):
    if p <= 3:
        return p == 2 or p == 3
    if p % 2 == 0:
        return False

    d = p - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randint(2, p - 2)
        x = szybkie_potegowanie(a, d, p)

        if x == 1 or x == p - 1:
            continue

        for _ in range(r - 1):
            x = szybkie_potegowanie(x, 2, p)
            if x == p - 1:
                break
        else:
            return False  # liczba na pewno jest złożona
    return True  # liczba prawdopodobnie jest pierwsza

if __name__ == "__main__":
    try:
        p = int(input("Wprowadź liczbę do testu pierwszości: "))
        k = int(input("Wprowadź liczbę prób (dokładność): "))

        wynik_fermata = test_fermata(p, k)
        wynik_miller_rabin = test_miller_rabin(p, k)

        print(f"\nTest Fermata: wprowadzona liczba {p} jest", "prawdopodobnie pierwsza" if wynik_fermata else "złożona")
        print(f"Test Millera-Rabina: wprowadzona liczba {p} jest", "prawdopodobnie pierwsza" if wynik_miller_rabin else "złożona")

    except ValueError:
        print("Bład! Wprowadź liczby naturalne.")

# Zadanie nr 5 – RSA
#  Zaimplementuj algorytm RSA. Zaszyfruj nim (i odszyfruj) przykładowe teksty. W razie potrzeby, automa
# tycznie dziel tekst na mniejsze, osobno szyfrowane części.
#  Wejście: tekst do zaszyfrowania/odszyfrowania.
#  Wyjście: zaszyfrowany/odszyfrowany tekst; klucz prywatny i klucz publiczny
print("Zadanie 5")
from math import gcd
def jest_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def odwrotnosc_modulo(a, m): # odwrotnosc modulo, rozszerzony algorytm euklidesa
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generuj_klucze():
    while True:
        p = random.randint(100, 500)
        q = random.randint(100, 500)
        if jest_pierwsza(p) and jest_pierwsza(q) and p != q:
            break

    n = p * q
    phi = (p - 1) * (q - 1) # zliczanie funckji eulera

    e = 65537 # popularny wybor => e: 1 < e < phi
    if gcd(e, phi) != 1:
        e = 3
        while gcd(e, phi) != 1:
            e += 2
    d = odwrotnosc_modulo(e, phi)

    return (e, n), (d, n)

def szyfrowania(text, public_key):
    e, n = public_key
    encrypted = []
    for char in text:
        m = ord(char)
        c = pow(m, e, n)
        encrypted.append(c)
    return encrypted

def odszyfrowania(cipher, private_key):
    d, n = private_key
    decrypted = ''
    for c in cipher:
        m = pow(c, d, n)
        decrypted += chr(m)
    return decrypted

def main():
    try:
        text = input("Wprowadź tekst do zaszyfrowania: ")

        print("Trwa generowanie kluczy RSA...")
        public_key, private_key = generuj_klucze()

        print(f"Klucz publiczny (e, n): {public_key}")
        print(f"Klucz prywatny (d, n): {private_key}")

        zaszyfrowane = szyfrowania(text, public_key)
        print("\nZaszyfrowany tekst (podany jako lista liczb):")
        print(zaszyfrowane)
        odszyfrowane = odszyfrowania(zaszyfrowane, private_key)
        print("\nRozszyfrowany tekst:")
        print(odszyfrowane)

    except Exception as e:
        print(f"Wystąpił błąd!: {e}")

if __name__ == "__main__":
    main()