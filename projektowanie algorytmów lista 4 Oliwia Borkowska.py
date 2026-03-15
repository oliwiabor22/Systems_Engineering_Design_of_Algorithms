# Projektowanie algorytmów lista nr 4 Oliwia Borkowska

# zadanie 1 Dla listy liczb zadanej przez użytkownika, zaimplementuj algorytm (algorytmy)
# 1. znajdujący największy element na liście,
# 2. znajdujący drugi największy element na liście,
# 3. obliczający średnią elementów na liście.
# Wejście: lista liczb.
# Wyjście: jak w punktach.
# Oszacuj złożoność czasową każdego z tych algorytmów


print("ZADANIE 1")

def wejscie():
    while True:
        user_input = input("Wprowadź liczby oddzielone przecinkami (np. 11, 25, 8.5): ")
        try:
            liczby = [float(x.strip()) for x in user_input.split(',')]
            if len(liczby) < 2:
                print("Wprowadź co najmniej dwie liczby.")
                continue
            return liczby
        except ValueError:
            print("Nieprawidłowe dane wejściowe. Upewnij się, że wprowadzasz tylko LICZBY oddzielone PRZECINKAMI.")

def najwieksza(liczby):
    max_liczba = liczby[0]
    for num in liczby[1:]:
        if num > max_liczba:
            max_liczba = num
    return max_liczba
# złożoność czasowa: O(n), gdzie n jest liczbą elementów na liście

def druga_najwieksza(liczby):
    first = second = float('-inf')
    for num in liczby:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    if second == float('-inf'):
        return None  # brak drugiego największego, wszystkie liczby są równe
    return second
# złożoność czasowa: O(n)

def srednia(liczby):
    return sum(liczby) / len(liczby)
# złożoność czasowa: O(n)

def main():
    liczby = wejscie()
    max_number = najwieksza(liczby)
    second_max = druga_najwieksza(liczby)
    average = srednia(liczby)

    print(f"Największy element z listy to: {max_number}")
    if second_max is not None:
        print(f"Drugi największy element z listy to: {second_max}")
    else:
        print("Nie można wyznaczyć drugiego największego elementu (wszystkie liczby są równe)")
    print(f"Średnia: {average}")

if __name__ == "__main__":
    main()

# zadanie 2 Zaimplementuj algorytm mnożący dwie macierze kwadratowe zadane przez użytkownika.
# Wejście: dwie macierze.
# Wyjście: wynik mnożenia.
# Oszacuj złożoność czasową algorytmu.

print("ZADANIE 2")


def macierz_input(n):
    matrix = []
    print(f"Wprowadź elementy macierzy {n} x {n} (oddzielaj elementy spacją):")
    for i in range(n):
        while True:
            try:
                row = input(f"Wiersz {i + 1}: ").split()
                row = [float(x) for x in row]
                if len(row) != n:
                    print(f"Macierz musi mieć {n} elementów w każdym wierszu")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Wprowadź LICZBY")
    return matrix

def mnozenie_macierzy(A, B):
    n = len(A)

# nowa macierz C
    C = [[0 for _ in range(n)] for _ in range(n)]

# mnożenie macierzy
    for i in range(n):
        for j in range(n):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(n))

    return C
def wyswietlenie_macierzy(matrix):
    for row in matrix:
        print("\t".join(f"{elem:.2f}" for elem in row)) # zaokrąglenie do dwóch miejsc po przecinku
def main():
    while True:
        try:
            n = int(input("Podaj rozmiar macierzy (n x n): "))
            if n <= 0:
                print("Błąd. Rozmiar macierzy musi być liczbą dodatnią.")
                continue
            break
        except ValueError:
            print("Wprowadź poprawną liczbę NATURALNĄ dla rozmiaru macierzy.")

    print("Macierz A:")
    A = macierz_input(n)
    print("Macierz B:")
    B = macierz_input(n)

    # mnożenie macierzy A i B
    C = mnozenie_macierzy(A, B)

    # Wypisujemy wynik
    print("Wynik mnożenia macierzy A i B (macierz C):")
    wyswietlenie_macierzy(C)

if __name__ == "__main__":
    main()

"""złożoność obliczeniowa algorytmu to O(n^3), ponieważ każdy element macierzy wynikowej (macierzy C) 
wymaga obliczenia sumy iloczynów dla n elementów. To oznacza, że każda operacja obejmuje n^2 elementów w macierzy C,
co daje złożoność O(n^3)."""

"""W ptzypadku bardzo dużych macierzy możnaby było zastosować algorytm Strassena, jednak wymaga on dużo pamięci i uwagi przy implementacji"""


# Zadanie 3 Dany jest zbiór liczb całkowitych A zadanych przez użytkownika. Zweryfikuj (testując wszystkie możliwe
# kombinacje) czy dla jakiegokolwiek podzbioru zbioru A suma liczb jest równa dokładnie 0.
# Wejście: zbiór liczb całkowitych
# Wyjście: odpowiedź, czy istnieją szukane podzbiory; jeśli tak - wyświetl je.
# Oszacuj złożoność czasową algorytmu.

print("ZADANIE 3")
import itertools
def zbior_liczb():
    while True:
        try:
            wejscie = input("Wprowadź liczby całkowite (oddzielone spacją) do zbioru A: ")
            liczby = [int(x) for x in wejscie.split()]
            if not liczby:
                print("Wprowadź przynajmniej jedną liczbę.")
                continue
            return liczby
        except ValueError:
            print("Wprowadź tylko liczby całkowite.")

def znalezienie_podzbioru_zero(liczby):
    zero_sum_subsets = []
    n = len(liczby)
    for r in range(1, n + 1):
        for subset in itertools.combinations(liczby, r):
            if sum(subset) == 0:
                zero_sum_subsets.append(subset)
    return zero_sum_subsets

def main():
    numbers = zbior_liczb()
    print("Szukanie podzbiorów, których suma wynosi 0...")

    result = znalezienie_podzbioru_zero(numbers)

    if result:
        print(f"Znaleziono {len(result)} podzbiorów zbioru A, których suma wynosi 0. Są to:")
        for subset in result:
            print(subset)
    else:
        print("Nie znaleziono żadnych podzbiorów, których suma wynosi 0 :(")

if __name__ == "__main__":
    main()
"""Dla n-elementowego zbioru istnieje 2^n wszytskich możliwych podzbiorów, jednak odejmujemy od tej liczby 1, 
ponieważ zbiór [] - pusty, nie jest brany pod uwagę. Jeśli istmieje 2^n - 1 podzbiorów, a sprawdzenie każdego z nich zajmuje
 O(n), to całkowita zlożonośc wynosi: O(n *(2^n - 1)), czyli O(n*2^n)"""

# zadanie 4 Dla programów napisanych w zadaniu nr 1 niech n będzie długością listy. Wykonaj czynności (napisz pro-
# gram):
# 1. dla n zadanego przez użytkownika wygeneruj (losowo) listę liczb (skorzystaj z wbudowanego generatora
# liczb losowych),
# 2. uruchom program z zadania nr 1 na wygenerowanej liście,
# 3. zwróć czas działania programu (z zadania nr 1, nie samej generacji listy) dla zadanego n.
# Powtórz czynności dla zadania nr 2 przyjmując za n rozmiar macierzy. Macierze generuj losowo.
# Powtórz czynności dla zadania nr 3 przyjmując za n długość listy. Listę generuj losowo.
# Wejście: n, wersja programu (z zadania nr 1, 2 lub 3 – może być w osobnych programach).
# Wyjście: czas działania programu.

print("ZADANIE 4")

import time
import random
import itertools

def czas_dzialania():
    print("Pomiar czasu działania wcześniej zaimplementowanych algorytmów")
    print("1 – Zadanie 1 (max element, drugi max element, średnia z listy)")
    print("2 – Zadanie 2 (mnożenie macierzy)")
    print("3 – Zadanie 3 (podzbiory o sumie 0)")

    try:
        wybor = int(input("Wybierz numer zadania (1–3): "))
        if wybor in [1, 3]:
            n = int(input("Podaj długość listy (n): "))
        elif wybor == 2:
            n = int(input("Podaj wymiary macierzy (n): "))
        else:
            print("Nie ma takiego zadania.")
            return
    except ValueError:
        print("Błąd: podaj liczbę całkowitą")
        return

    if wybor == 1:
        liczby = [random.uniform(-100, 100) for _ in range(n)]
        print(f"\nWylosowana lista: {liczby}")
        start = time.time()
        najwieksza(liczby)
        druga_najwieksza(liczby)
        srednia(liczby)
        end = time.time()
        print(f"Czas działania zadania 1: {end - start} sekund")

    elif wybor == 2:
        def generuj_macierz(n):
            return [[random.randint(-10, 10) for _ in range(n)] for _ in range(n)]

        def mnoz_macierze(A, B):
            wynik = [[0 for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        wynik[i][j] += A[i][k] * B[k][j]
            return wynik

        A = generuj_macierz(n)
        B = generuj_macierz(n)
        print("\nMacierz A:")
        for row in A:
            print(row)
        print("\nMacierz B:")
        for row in B:
            print(row)

        start = time.time()
        mnoz_macierze(A, B)
        end = time.time()
        print(f"Czas działania zadania 2: {end - start} sekund")

    elif wybor == 3:
        liczby = [random.randint(-15, 15) for _ in range(n)]
        print(f"\nWylosowana lista: {liczby}")

        def znajdz_podzbiory_sumujace_sie_do_zera(liczby):
            podzbiory = []
            for r in range(1, len(liczby) + 1):
                for kombinacja in itertools.combinations(liczby, r):
                    if sum(kombinacja) == 0:
                        podzbiory.append(kombinacja)
            return podzbiory

        start = time.time()
        znajdz_podzbiory_sumujace_sie_do_zera(liczby)
        end = time.time()
        print(f"Czas działania zadania 3: {end - start} sekund")

if __name__ == "__main__":
    czas_dzialania()

# zadanie 5
# Dla każdej wersji zadania nr 4, czyli dla problemów z zadań 1, 2 i 3 wykonaj:
# • dla każdego n ∈ {1, 2, 3, . . . , 10} uruchom program po 10 razy,
# • na wykresie od n (oś odciętych) wyświetl średni, minimalny i maksymalny czas działania algorytmu,
# • przerwij działanie programu, jeśli wykonuje się dłużej niż 10 minut; ogranicz wykresy tylko do uzyska-
# nych rezultatów,
# • zestaw wykresy ze złożonością oszacowaną analitycznie.
# Wyjście: 3 układy współrzędnych (dla problemów z zadań 1, 2, 3), każdy po 3 wykresy (średni, minimalny i
# maksymalny czas działania)
print("ZADANIE 5")
import time
import random
import itertools
import matplotlib.pyplot as plt
import math

def zadanie1_algorytm(liczby):
    najwieksza(liczby)
    druga_najwieksza(liczby)
    srednia(liczby)
def zadanie2_algorytm(A, B):
    mnozenie_macierzy(A, B)
def zadanie3_algorytm(liczby):
    znalezienie_podzbioru_zero(liczby)

# pomiary czasu
def zmierz_czasy_zadania(funkcja, dane_generator, n_values):
    srednie, minima, maksima = [], [], []
    for n in n_values:
        czasy = []
        for _ in range(10):
            dane = dane_generator(n)
            start = time.time()
            funkcja(*dane) if isinstance(dane, tuple) else funkcja(dane)
            end = time.time()
            czas = end - start
            if czas > 600:
                print(f"Przerwano dla n={n} ze względu na zbyt długi czas (>10 minut)")
                return n_values[:len(srednie)], srednie, minima, maksima
            czasy.append(czas)
        srednie.append(sum(czasy) / 10)
        minima.append(min(czasy))
        maksima.append(max(czasy))
    return n_values, srednie, minima, maksima

def gen_lista_zad1(n):
    return [random.uniform(-100, 100) for _ in range(n)]

def gen_macierze_zad2(n):
    A = [[random.randint(-10, 10) for _ in range(n)] for _ in range(n)]
    B = [[random.randint(-10, 10) for _ in range(n)] for _ in range(n)]
    return A, B

def gen_lista_zad3(n):
    return [random.randint(-15, 15) for _ in range(n)]
def rysuj_wykres(n_values, srednie, minima, maksima, tytul, teoretyczna_funkcja=None, etykieta_zlozonosci=""):
    plt.figure()
    plt.plot(n_values, srednie, label='Średni czas', marker='o', color="blue")
    plt.plot(n_values, minima, label='Minimalny czas', color="red")
    plt.plot(n_values, maksima, label='Maksymalny czas', linestyle='--', color="magenta")
    if teoretyczna_funkcja:
        plt.plot(n_values, [teoretyczna_funkcja(n) for n in n_values], label=f'Teoretyczna ({etykieta_zlozonosci})', linestyle='dotted')
    plt.xlabel('n')
    plt.ylabel('Czas [s]')
    plt.title(tytul)
    plt.legend()
    plt.grid(True)
    plt.show()

def zadanie5():
    n_values = list(range(1, 11))

    # zadanie 1 – O(n)
    n1, sr1, min1, max1 = zmierz_czasy_zadania(zadanie1_algorytm, gen_lista_zad1, n_values)
    rysuj_wykres(n1, sr1, min1, max1, "Zadanie 1: lista – max, drugi max, średnia", lambda n: n * 1e-6, "O(n)")

    # zadanie 2 – O(n^3)
    n2, sr2, min2, max2 = zmierz_czasy_zadania(zadanie2_algorytm, gen_macierze_zad2, n_values)
    rysuj_wykres(n2, sr2, min2, max2, "Zadanie 2: mnożenie macierzy", lambda n: (n**3) * 1e-7, "O(n^3)")

    # zadanie 3 – O(n * 2^n)
    n3, sr3, min3, max3 = zmierz_czasy_zadania(zadanie3_algorytm, gen_lista_zad3, n_values)
    rysuj_wykres(n3, sr3, min3, max3, "Zadanie 3: podzbiory o sumie 0", lambda n: n * (2**n) * 1e-8, "O(n*2^n)")
zadanie5()
