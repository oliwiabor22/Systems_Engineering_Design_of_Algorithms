# Oliwia Borkowska projektowanie algorytmów lista 5 - algorytmy rekurencyjne

# Zadanie 1 Dla następujących ciągów liczbowych: * 3 ciągi* wykonaj:
# 1. zaimplementuj (rekurenycjny) algorytm wyliczający wartość ntego elementu ciągu,
# 2. analitycznie wyznacz wzór na wartość ntego elementu ciągu (np. indukcyjnie),
# 3. napisz procedurę weryfikującą poprawność zaimplementowanej rekurencji (wyświetlającą i porównującą
# wynik numeryczny i analityczny) dla N pierwszych elementów ciągu (N zadane przez użytkownika).
# Wejście: N .
# Wyjście: zestawienie wartości wyliczanych algorytmem rekurencyjnym i ze wzoru.
print("Zadanie 1")
import math

# ciąg 1: x(n) = 3n + x(n-1), x(0) = 1
def alg_rekurencyjny1(n):
    if n == 0:
        return 1
    return 3 * n + alg_rekurencyjny1(n - 1)

def formula1(n):
    # Rozwijając rekurencję, wychodzi wzór: x(n) = (3 * n * (n + 1)) / 2 + 1
    return (3 * n * (n + 1)) // 2 + 1

# ciąg 2: x(n) = n + x(n-2), x(−1) = x(0) = 0
def alg_rekurencyjny2(n):
    if n <= 0:
        return 0
    return n + alg_rekurencyjny2(n - 2)

def formula2(n):
    # jeśli n parzyste to suma parzystych liczb
    # jeśli n nieparzyste to suma nieparzystych liczb
    if n % 2 == 0:
        k = n // 2
        return k * (k + 1)
    else:
        k = (n + 1) // 2
        return k * k

# ciąg f: x(n) = x(n-1) + x(n-2), x(1) = 1, x(0) = 0
def ciag_fibonacciego(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return ciag_fibonacciego(n - 1) + ciag_fibonacciego(n - 2)

def formula_c_fibonnaciego(n):
    # Wzór Binetta
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    return int(round((phi**n - psi**n) / math.sqrt(5)))

# procedura weryfikująca
def weryf_poprawnosci(seq_name, recursive_func, formula_func, N):
    print(f"\nWeryfikacja ciągu {seq_name}:")
    print(f"{'n':>3} | {'Rekurencyjnie':>15} | {'Wzór':>10} | {'Czy zgodne?':>5}")
    print("-" * 42)
    for n in range(N):
        rec = recursive_func(n)
        form = formula_func(n)
        ok = rec == form
        print(f"{n:>3} | {rec:>15} | {form:>10} | {str(ok):>5}")

def main():
    while True:
        try:
            N = int(input("Podaj N (liczbę elementów do sprawdzenia): "))
            if N < 0:
                print("Podaj liczbę nieujemną!")
                continue
            break
        except ValueError:
            print("Błąd: podaj poprawną liczbę całkowitą!")

    weryf_poprawnosci("1: x(n) = 3n + x(n-1)", alg_rekurencyjny1, formula1, N)
    weryf_poprawnosci("2: x(n) = n + x(n-2)", alg_rekurencyjny2, formula2, N)
    weryf_poprawnosci("3: Ciąg Fibonacciego", ciag_fibonacciego, formula_c_fibonnaciego, N)

if __name__ == "__main__":
    main()


# Zadanie 2 Dla listy liczb zadanej przez użytkownika, zaimplementuj algorytm (algorytmy) rekurencyjne
# 1. znajdujący największy element na liście,
# 2. znajdujący drugi największy element na liście,
# 3. obliczający średnią elementów na liście.
# Algorytmy dzielą listę na dwie (w przybliżeniu) połowy i uruchamiają się rekurencyjnie na utworzonych
# połowach.
# Wejście: lista liczb.
# Wyjście: jak w 1, 2, 3.
# Oszacuj złożoność czasową algorytmów.
print("Zadanie 2")

# algorytm rekurencyjny znajdujący największy element na liście
def znajdz_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        mid = len(lst) // 2
        left_max = znajdz_max(lst[:mid])
        right_max = znajdz_max(lst[mid:])
        return left_max if left_max > right_max else right_max

# algorytm rekurencyjny znajdujący drugi największy element
def znajdz_drugi_max(lst):
    if len(lst) < 2:
        return None # jeśli nie ma
    if len(lst) == 2:
        return min(lst)

    mid = len(lst) // 2
    left_second = znajdz_drugi_max(lst[:mid])
    right_second = znajdz_drugi_max(lst[mid:])
    left_max = znajdz_max(lst[:mid])
    right_max = znajdz_max(lst[mid:])

# max z kandydatow
    candidates = [left_max, right_max]
    if left_second is not None:
        candidates.append(left_second)
    if right_second is not None:
        candidates.append(right_second)

    candidates = list(set(candidates)) # usuniecie duplikatow
    candidates.sort(reverse=True)

    if len(candidates) >= 2:
        return candidates[1]
    else:
        return None


# suma elementow
def suma_rekurencyjna(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    else:
        mid = len(lst) // 2
        return suma_rekurencyjna(lst[:mid]) + suma_rekurencyjna(lst[mid:])

def srednia(lst):
    if len(lst) == 0:
        return None # zabezpieczenie dzielenia przez 0
    suma = suma_rekurencyjna(lst)
    return suma / len(lst)


def wczytaj_liste():
    while True:
        wejscie = input("Podaj listę liczb oddzielonych spacjami: ")
        try:
            lista = [float(x) for x in wejscie.strip().split()]
            if not lista:
                print("Lista jest pusta, wprowadź liczby!!!")
                continue
            return lista
        except ValueError:
            print("Błąd: wprowadź tylko liczby oddzielone spacjami!!!")

def main():
    lista = wczytaj_liste()

    maksimum = znajdz_max(lista)
    drugie_maksimum = znajdz_drugi_max(lista)
    srednia_lista = srednia(lista)

    print(f"Największy element: {maksimum}")
    if drugie_maksimum is not None:
        print(f"Drugi największy element: {drugie_maksimum}")
    else:
        print("Drugi największy element: brak (za mało elementów).")
    print(f"Średnia elementów: {srednia_lista:.2f}")


if __name__ == "__main__":
    main()

# Zadanie 3 Zaimplementuj algorytm sortowania przez scalanie wykonywany na liście liczb zadanej przez użytkownika.
# Wejście: lista liczb
# Wyjście: posortowana lista liczb.
print("Zadanie 3")

def merge_sort(lst): # sortowanie przez scalanie
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right): # scalanie dwóch list
    wynik = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            wynik.append(left[i])
            i += 1
        else:
            wynik.append(right[j])
            j += 1

    wynik.extend(left[i:])
    wynik.extend(right[j:])

    return wynik

def wczytaj_liste():
    while True:
        wejscie = input("Podaj listę liczb oddzielonych spacjami: ")
        try:
            lista = [float(x) for x in wejscie.strip().split()]
            if not lista:
                print("Lista jest pusta, wprowadź liczby!!!")
                continue
            return lista
        except ValueError:
            print("Błąd: wprowadź tylko liczby oddzielone spacjami!!!")

def main():
    lista = wczytaj_liste()
    print("\nLista przed sortowaniem:")
    print(lista)
    posortowana = merge_sort(lista)
    print("\nLista po sortowaniu przez sacalanie (w kolejności rosnącej):")
    print(posortowana)

if __name__ == "__main__":
    main()

# Zadanie 4. Dany jest graf nieskierowany, nieważony. Niech długość ścieżki będzie liczbą krawędzi na niej.
# Zaimplementuj rekurencyjną metodę wyznaczania najkrótszej ścieżki między dwoma zadanymi wierzchoł-
# kami.
# Jeśli wierzchołki nie są bezpośrednimi sąsiadami, metoda wywołuje się rekurencyjnie, na każdym z bezpo-
# średnich sąsiadów pierwszego wierzchołka i na drugim wierzchołku.
# Jeśli wierzchołki są bezpośrednimi sąsiadami zwracana odległość to 1.
# Uwaga: zadbaj o to, żeby wierzchołków nie odwiedzać wielokrotnie i o to, żeby algorytm nie zapętlał się w
# nieskończoność (a dokładniej, do przepełnienia stosu).
# Wejście: graf zadany w pliku (zaproponuj format pliku).
# Wyjście: najkrótsza ścieżka i jej długość.
# Oszacuj złożoność czasową algorytmu.
print("Zadanie 4")

import networkx as nx
import matplotlib.pyplot as plt

def wczytaj_graf_do_slownika(nazwa_pliku):
    graf = {}
    with open(nazwa_pliku, 'r') as plik:
        for linia in plik:
            linia = linia.strip()
            if linia:
                wierzcholek, sasiedzi = linia.split(":")
                wierzcholek = wierzcholek.strip()
                sasiedzi = [sasiad.strip() for sasiad in sasiedzi.split()]
                graf[wierzcholek] = sasiedzi
    return graf

def slownik_na_networkx(graf_slownik): # zamiania powrotna - z grafu na słownik
    G = nx.Graph()
    for wierzcholek, sasiedzi in graf_slownik.items():
        for sasiad in sasiedzi:
            G.add_edge(wierzcholek, sasiad)
    return G

def znajdz_najkrotsza_sciezke(graf, start, cel, odwiedzone=None):
    if odwiedzone is None:
        odwiedzone = set()
    if start == cel:
        return [start]
    odwiedzone.add(start)

    najkrotsza_sciezka = None

    for sasiad in graf.get(start, []): # jesli jest sasiadem
        if sasiad not in odwiedzone:
            sciezka = znajdz_najkrotsza_sciezke(graf, sasiad, cel, odwiedzone.copy())
            if sciezka:
                sciezka = [start] + sciezka
                if (najkrotsza_sciezka is None) or (len(sciezka) < len(najkrotsza_sciezka)):
                    najkrotsza_sciezka = sciezka

    return najkrotsza_sciezka

def rysuj_graf(graf_nx, sciezka=None): # rysowanie grafu z podswietlonymi krawedziami
    pos = nx.spring_layout(graf_nx)

    plt.figure(figsize=(8, 6))

    nx.draw(graf_nx, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=12, font_weight="bold", edge_color="gray")

    if sciezka and len(sciezka) >= 2:
        edges_in_path = list(zip(sciezka, sciezka[1:]))
        nx.draw_networkx_edges(graf_nx, pos, edgelist=edges_in_path, edge_color='red', width=4)

    plt.title("Graf z najkrótszą ścieżką" if sciezka else "Graf")
    plt.show()

def main():
    nazwa_pliku = input("Podaj nazwę pliku z grafem (np. graf.txt): ").strip()
    graf_slownik = wczytaj_graf_do_slownika(nazwa_pliku)
    graf_nx = slownik_na_networkx(graf_slownik)

    start = input("Podaj wierzchołek startowy: ").strip()
    koniec = input("Podaj wierzchołek końcowy: ").strip()

    if start not in graf_slownik or koniec not in graf_slownik:
        print("Podano nieprawidłowe wierzchołki!")
        return

    # 3. Znalezienie najkrótszej ścieżki
    sciezka = znajdz_najkrotsza_sciezke(graf_slownik, start, koniec)

    if sciezka:
        print("\nNajkrótsza ścieżka:", " -> ".join(sciezka))
        print("Długość ścieżki:", len(sciezka) - 1)
    else:
        print("\nBrak ścieżki między tymi wierzchołkami!")

    rysuj_graf(graf_nx, sciezka)

if __name__ == "__main__":
    main()

# Zadanie 5.  Wyświetl wykresy czasu działania programów z zadań nr 2 i 3 w zależności od rozmiaru wejścia.
# Dane wejściowe (listy liczb) generuj losowo.
# Wyjście: wykresy czasu działania.
print("Zadanie 5")

import random
import time
import matplotlib.pyplot as plt

def pomiar_czasu(funkcja, lista):
    start = time.perf_counter()
    funkcja(lista)
    end = time.perf_counter()
    return end - start

def main():
    rozmiary = [10, 50, 100, 200, 500, 1000, 2000, 5000]
    czasy_max = []
    czasy_drugi_max = []
    czasy_srednia = []
    czasy_merge_sort = []

    for rozmiar in rozmiary:
        lista = [random.uniform(-1000, 1000) for _ in range(rozmiar)]

        czasy_max.append(pomiar_czasu(znajdz_max, lista))
        czasy_drugi_max.append(pomiar_czasu(znajdz_drugi_max, lista))
        czasy_srednia.append(pomiar_czasu(srednia, lista))
        czasy_merge_sort.append(pomiar_czasu(merge_sort, lista))

    plt.figure(figsize=(12, 8))
    plt.plot(rozmiary, czasy_max, label="Znajdowanie maksimum")
    plt.plot(rozmiary, czasy_drugi_max, label="Znajdowanie drugiego maksimum")
    plt.plot(rozmiary, czasy_srednia, label="Obliczanie średniej")
    plt.plot(rozmiary, czasy_merge_sort, label="Sortowanie przez scalanie (Merge Sort)")

    plt.xlabel("Rozmiar listy")
    plt.ylabel("Czas wykonania w sekundach")
    plt.title("Wykres czasów działania algorytmów z zadania 2 i 3")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()

# w tym przypadku alg znajdz_drugie_max ma największą złożoność czasową, a to wynika z faktu, że na każdym poziomie
# dodatkowo szukane jest maximum. Aby to zmienić możnaby zaimplementować to w taki sposób, aby podczas szukania maksimum od razu zapamiętywać
# także to drugie maximum