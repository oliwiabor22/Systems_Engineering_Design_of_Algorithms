# projektowanie algorytmów Oliwia Borkowska lista 8 - Stosy, kolejki, listy, grafy i zbiory rozłączne
import random
import json
from tabulate import tabulate
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

# zadanie 1: Pojedynczy robot jest krotką o polach (parametrach):
# (a) TYP – tekst ze zbioru {„AGV”, „AFV”, „ASV”, „AUV” },
# (b) CENA – liczba rzeczywista z przedziału [0, 10000] (PLN),
# (c) ZASIĘG – liczba całkowita z przedziału [0, 100] (km),
# (d) KAMERA – wartość binarna {0, 1} (jest, nie ma).
# 2. Przygotuj procedurę do generacji listy N robotów o losowo zadanych parametrach.
# 3. Wyświetl listę robotów i ich parametry (w tabelce: jeden robot – jeden wiersz).
# 4. Zaimplementuj funkcję zapisującą/odczytującą strukturę do/z pliku
# Wejście: długość listy N .
# Wyjście: lista robotów wyświetlona na ekranie i zapisana do pliku

print("Zadanie 1")

TYPY_ROBOTÓW = ["AGV", "AFV", "ASV", "AUV"]
PLIK = "roboty.json"

def generuj_robota():
    return {
        "TYP": random.choice(TYPY_ROBOTÓW),
        "CENA": round(random.uniform(0, 10000), 2),
        "ZASIĘG": random.randint(0, 100),
        "KAMERA": random.randint(0, 1)
    }

def pobierz_liczbe_robotow():
    while True:
        wejscie = input("Podaj liczbę robotów do wygenerowania: ")
        if wejscie.isdigit():
            return int(wejscie)
        else:
            print("Błąd: podaj poprawną liczbę naturalną!")

def generuj_liste_robotow(n):
    return [generuj_robota() for _ in range(n)]

def wyswietlanie_robotow(roboty):
    print("\nLista robotów:")
    print(tabulate(roboty, headers="keys", tablefmt="grid"))

def zapisz_do_pliku(roboty, PLIK):
    with open(PLIK, "w", encoding="utf-8") as f:
        json.dump(roboty, f, ensure_ascii=False, indent=4)

def odczytaj_z_pliku(PLIK):
    with open(PLIK, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    n = pobierz_liczbe_robotow()
    roboty = generuj_liste_robotow(n)
    wyswietlanie_robotow(roboty)
    zapisz_do_pliku(roboty, PLIK)
    print(f"\nZapisano do pliku '{PLIK}'.")
    print("\nOdczyt z pliku:")
    odczytane_roboty = odczytaj_z_pliku(PLIK)
    wyswietlanie_robotow(odczytane_roboty)

if __name__ == "__main__":
    main()

# zadanie 2. Zaimplementuj stos do przechowywania informacji o robotach.
# Zaimplementuj algorytmy
# • dodawania robota do stosu (parametry robota zadaje użytkownik),
# • usuwania robota ze stosu i wyświetlenia jego parametrów,
# • wyczyszczenia stosu i wyświetlenia parametrów wszystkich usuniętych robotów.
# Wejście: pusty stos robotów.
# Wyjście: stos robotów z dodanymi/usuniętymi robotami.

print("zadanie 2")

def wczytanie_typu():
    typy = ["AGV", "AFV", "ASV", "AUV"]
    while True:
        typ = input(f"Podaj typ robota ({', '.join(typy)}): ").strip().upper()
        if typ in typy:
            return typ
        print("Nieprawidłowy typ. Wpisz typ ponownie.")

def wczytanie_ceny():
    while True:
        try:
            cena = float(input("Podaj cenę robota w zakresie od 0–10000 zł: "))
            if 0 <= cena <= 10000:
                return round(cena, 2)
            else:
                print("Cena musi być w zakresie 0–10000.")
        except ValueError:
            print("Błąd: wprowadź liczbę!.")

def wczytanie_zasiegu():
    while True:
        try:
            zasieg = int(input("Podaj zasięg robota w zakresie od 0–100 km: "))
            if 0 <= zasieg <= 100:
                return zasieg
            else:
                print("Zasięg musi być w zakresie od 0–100.")
        except ValueError:
            print("Błąd: wprowadź liczbę całkowitą!")

def wczytanie_kamery():
    while True:
        kamera = input("Czy robot ma kamerę? 1 - tak, 0 - nie: ")
        if kamera in ["0", "1"]:
            return int(kamera)
        print("Błąd: Podaj tylko 0 lub 1!")

def dodanie_robota_na_stos(stos):
    print("Dodawanie robota")
    robot = {
        "TYP": wczytanie_typu(),
        "CENA": wczytanie_ceny(),
        "ZASIĘG": wczytanie_zasiegu(),
        "KAMERA": wczytanie_kamery()
    }
    stos.append(robot)
    print("Robot został dodany na stos.")

def usuwanie_robota_ze_stosu(stos):
    print("Usuwanie robota")
    if stos:
        robot = stos.pop()
        print("Usunięto robota ze stosu:")
        print(robot)
    else:
        print("Stos jest już pusty. Nie ma nic do usunięcia.")

def wyczyszczenie_stosu(stos):
    print("Czyszczenie stosu")
    if stos:
        print("Usuwanie wszystkich robotów:")
        while stos:
            robot = stos.pop()
            print(robot)
        print("Stos został wyczyszczony.")
    else:
        print("Stos już jest pusty.")

def wyswietlanie_stosu(stos):
    print("Zawartość stosu")
    if not stos:
        print("Stos jest pusty.")
    else:
        for i, robot in enumerate(reversed(stos), 1):
            print(f"{i}. {robot}")
def main():
    stos = []
    while True:
        print("MENU:")
        print("0. Wyjście")
        print("1. Dodaj robota na stos")
        print("2. Usuń robota ze stosu")
        print("3. Wyczyszczenie stosu")
        print("4. Wyświetl stos")
        wybor = input("Wybierz opcję: ")
        if wybor == "1":
            dodanie_robota_na_stos(stos)
        elif wybor == "2":
            usuwanie_robota_ze_stosu(stos)
        elif wybor == "3":
            wyczyszczenie_stosu(stos)
        elif wybor == "4":
            wyswietlanie_stosu(stos)
        elif wybor == "0":
            print("Zamykanie programu...")
            print("Zamknięto program STOS.")
            break
        else:
            print("Nie ma takiej opcji. Spróbuj ponownie.")

if __name__ == "__main__":
    main()

# zadanie 3. Wykorzystaj dane z poprzednich list (flota robotów).
# Zaimplementuj kolejkę do przechowywania informacji o robotach.
# Zaimplementuj algorytmy
# • dodawania robota do kolejki (parametry robota zadaje użytkownik),
# • usuwania robota ze kolejki i wyświetlenia jego parametrów,
# • wyczyszczenia kolejki i wyświetlenia parametrów wszystkich usuniętych robotów.
# Wejście: pusta kolejka robotów.
# Wyjście: kolejka robotów z dodanymi/usuniętymi robotami.

print("zadanie 3")
def dodanie_robota_do_kolejki(kolejka):
    print("Dodawanie robota do kolejki")
    robot = {
        "TYP": wczytanie_typu(),
        "CENA": wczytanie_ceny(),
        "ZASIĘG": wczytanie_zasiegu(),
        "KAMERA": wczytanie_kamery()
    }
    kolejka.append(robot)
    print("Robot został dodany do kolejki.")

def usuwanie_robota_z_kolejki(kolejka):
    print(" Usuwanie robota z kolejki")
    if kolejka:
        robot = kolejka.popleft()
        print("Usunięto robota z kolejki.")
        print(robot)
    else:
        print("Kolejka jest już pusta. Nie ma nic do usunięcia.")


def wyczyszczenie_kolejki(kolejka):
    print("Czyszczenie kolejki")
    if kolejka:
        print("Usuwanie wszystkich robotów.")
        while kolejka:
            robot = kolejka.popleft()
            print(robot)
        print("Kolejka została wyczyszczona.")
    else:
        print("Kolejka jest już pusta.")

def wyswietlenie_kolejki(kolejka):
    print("Kolejka")
    if not kolejka:
        print("Kolejka jest pusta.")
    else:
        for i, robot in enumerate(kolejka, 1):
            print(f"{i}. {robot}")

def main():
    kolejka = deque()
    while True:
        print("MENU:")
        print("0. Wyjście")
        print("1. Dodaj robota do kolejki")
        print("2. Usuń robota z kolejki")
        print("3. Wyczyszczenie kolejki")
        print("4. Wyświetl kolejkę")
        wybor = input("Wybierz opcję: ")
        if wybor == "1":
            dodanie_robota_do_kolejki(kolejka)
        elif wybor == "2":
            usuwanie_robota_z_kolejki(kolejka)
        elif wybor == "3":
            wyczyszczenie_kolejki(kolejka)
        elif wybor == "4":
            wyswietlenie_kolejki(kolejka)
        elif wybor == "0":
            print("Zamykanie programu...")
            print("Zamknięto program KOLEJKA.")
            break
        else:
            print("Nie ma takiej opcji. Spróbuj ponownie.")

if __name__ == "__main__":
    main()

# zadanie 4. Zaimplementuj listę z dowiązaniami do reprezentacji floty robotów. Zaproponuj postać klucza. Do przecho-
# wywania listy zastosuj reprezentację tablicową.
# Zaimplementuj algorytmy
# • dodawania elementu do listy,
# • usuwania elementu z listy,
# • wyszukiwania elementu na liście (i wyświetlania jego parametrów).
# Wejście: pusta lista z dowiązaniami.
# Wyjście: lista z dodanymi/usuniętymi robotami.

print("zadanie 4")


def dodanie_robota(flota, indeks_startowy):
    klucz = input("Wprowadź unikalny klucz robota (np. 001): ").strip()

    for robot in flota:
        if robot["KLUCZ"] == klucz:
            print("Robot o takim kluczu już istnieje. Zmień klucz na jeszcze niesitniejący.")
            return indeks_startowy

    nowy_robot = {
        "KLUCZ": klucz,
        "DANE": {
            "TYP": wczytanie_typu(),
            "CENA": wczytanie_ceny(),
            "ZASIĘG": wczytanie_zasiegu(),
            "KAMERA": wczytanie_kamery()
        },
        "NASTEPNY": None
    }

    if not flota:
        flota.append(nowy_robot)
        return 0
    else:
        for i in range(len(flota)):
            if flota[i]["NASTEPNY"] is None:
                flota[i]["NASTEPNY"] = len(flota)
                break
        flota.append(nowy_robot)
        return indeks_startowy


def usuwanie_robota(flota, indeks_startowy):
    klucz = input("Wprowadź klucz robota do usunięcia: ").strip()

    if indeks_startowy is None:
        print("Lista jest pusta.")
        return indeks_startowy

    poprzedni = None
    aktualny = indeks_startowy

    while aktualny is not None:
        robot = flota[aktualny]
        if robot["KLUCZ"] == klucz:
            if poprzedni is None:
                indeks_startowy = robot["NASTEPNY"]
            else:
                flota[poprzedni]["NASTEPNY"] = robot["NASTEPNY"]
            print(f"Usunięto robota: {robot}")
            return indeks_startowy
        poprzedni = aktualny
        aktualny = robot["NASTEPNY"]

    print("Nie odnalezniono robota o podanym kluczu.")
    return indeks_startowy

def wyszukanie_robota(flota, indeks_startowy):
    klucz = input("Podaj klucz robota, którego chcesz wyszukać: ").strip()
    aktualny = indeks_startowy

    while aktualny is not None:
        robot = flota[aktualny]
        if robot["KLUCZ"] == klucz:
            print("Znaleziono robota:")
            print(f"KLUCZ: {robot['KLUCZ']}")
            for k, v in robot["DANE"].items():
                print(f"{k}: {v}")
            return
        aktualny = robot["NASTEPNY"]

    print("Nie znaleziono tego robota.")


def wyswietlenie_floty(flota, indeks_startowy):
    print("Lista robotów:")
    if indeks_startowy is None:
        print("Lista jest pusta.")
        return

    print(f"{'KLUCZ':<10} {'TYP':<5} {'CENA':<10} {'ZASIĘG (km)':<12} {'KAMERA':<8}")
    print("-" * 50)

    aktualny = indeks_startowy
    while aktualny is not None:
        robot = flota[aktualny]
        dane = robot["DANE"]
        print(f"{robot['KLUCZ']:<10} {dane['TYP']:<5} {dane['CENA']:<10.2f} {dane['ZASIĘG']:<12} {dane['KAMERA']:<8}")
        aktualny = robot["NASTEPNY"]

def main():
    flota = []
    indeks_startowy = None

    while True:
        print("MENU:")
        print("0. Wyjście")
        print("1. Dodaj robota")
        print("2. Usuń robota")
        print("3. Wyszukaj robota")
        print("4. Wyświetl całą flotę")

        wybor = input("Wybierz opcję: ")
        if wybor == "1":
            indeks_startowy = dodanie_robota(flota, indeks_startowy)
        elif wybor == "2":
            indeks_startowy = usuwanie_robota(flota, indeks_startowy)
        elif wybor == "3":
            wyszukanie_robota(flota, indeks_startowy)
        elif wybor == "4":
            wyswietlenie_floty(flota, indeks_startowy)
        elif wybor == "0":
            print("Zamykanie programu...")
            print("Zamyknięto program.")
            break
        else:
            print("Nie ma takiej opcji. Spróbuj ponownie.")

if __name__ == "__main__":
    main()

# zadanie 5: Pobierz od użytkownika graf nieskierowany (dowolna struktura, może być z pliku). Wykorzystaj zbiory
# rozłączne do weryfikacji czy dwa wierzchołki zadanego grafu należą do jednej spójnej składowej.
# Wyświetl listy wierzchołków tworzących spójne składowe.
# Wejście: Graf nieskierowany.
# Wyjście: listy wierzchołków tworzących spójne składowe.

print("zadanie 5")

class ZbioryRozłączne:
    def __init__(self):
        self.rodzic = {}

    def znajdz(self, x):
        if self.rodzic[x] != x:
            self.rodzic[x] = self.znajdz(self.rodzic[x])
        return self.rodzic[x]

    def polacz(self, x, y):
        korzen_x = self.znajdz(x)
        korzen_y = self.znajdz(y)
        if korzen_x != korzen_y:
            self.rodzic[korzen_y] = korzen_x

    def dodaj(self, x):
        if x not in self.rodzic:
            self.rodzic[x] = x

    def pobranie_skladnikow(self):
        skladniki = {}
        for x in self.rodzic:
            korzen = self.znajdz(x)
            if korzen not in skladniki:
                skladniki[korzen] = []
            skladniki[korzen].append(x)
        return skladniki


def wczytaj_graf_z_pliku(nazwa_pliku):
    graf = {}
    try:
        with open(nazwa_pliku, 'r') as plik:
            for linia in plik:
                if ':' in linia:
                    wierzcholek, sasiedzi = linia.strip().split(':')
                    graf[wierzcholek.strip()] = [s.strip() for s in sasiedzi.strip().split()]
    except FileNotFoundError:
        print("Błąd: Nie znaleziono pliku! Spróbuj ponowanie.")
        exit(1)
    return graf


def znajdowanie_spojnych_skladowych(graf):
    zb = ZbioryRozłączne()

    for wierzcholek in graf:
        zb.dodaj(wierzcholek)
        for sasiad in graf[wierzcholek]:
            zb.dodaj(sasiad)
            zb.polacz(wierzcholek, sasiad)

    return zb.pobranie_skladnikow()

def wizualizuj_graf(graf):
    G = nx.Graph()
    for wierzcholek, sasiedzi in graf.items():
        for sasiad in sasiedzi:
            G.add_edge(wierzcholek, sasiad)

    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='magenta', node_size=1200, font_size=12)
    plt.title("Wizualizacja grafu")
    plt.show()

def main():
    nazwa_pliku = input("Podaj nazwę pliku z twoim grafem (przykładowo: graf.txt): ").strip()
    graf = wczytaj_graf_z_pliku(nazwa_pliku)

    wizualizuj_graf(graf)

    skladniki = znajdowanie_spojnych_skladowych(graf)

    print("Spójne składowe grafu:")
    for i, (reprezentant, wierzcholki) in enumerate(skladniki.items(), 1):
        print(f"Składowa {i}: {', '.join(sorted(wierzcholki))}")


if __name__ == "__main__":
    main()