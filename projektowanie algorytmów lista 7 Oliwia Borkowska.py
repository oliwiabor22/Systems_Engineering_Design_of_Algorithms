# projektowanie algorytmów Oliwia Borkowska - lista 7 FFT

# Zadanie nr 1 – mnożenie wielomianów
# Zaimplementuj naiwną procedurę mnożenia wielomianów reprezentowanych przez współczynniki.
# Wejście: dwie listy współczynników wielomianu.
# Wyjście: lista współczynników wielomianu.

print("Zadanie 1 - naiwne mnozenie wielomianow")

import numpy as np
def naiwne_mnozenie_wielomianow(A, B):
    n = len(A)
    m = len(B)
    result = [0] * (n + m - 1)

    for i in range(n):
        for j in range(m):
            result[i + j] += A[i] * B[j]

    return result

def zadanie1():
    A = list(map(float, input("Podaj współczynniki pierwszego wielomianu (oddzielone spacją): ").split()))
    B = list(map(float, input("Podaj współczynniki drugiego wielomianu (oddzielone spacją): ").split()))

    result = naiwne_mnozenie_wielomianow(A, B)
    print("Wynik - lista współczynnikó wielomianu:", result)

if __name__ == "__main__":
    zadanie1()

# Zadanie nr 2 – FFT
# Zaimplementuj szybki algorytm wyznaczania dyskretnej transformaty Fouriera (FFT).
# Wejście: lista próbek sygnału.
# Wyjście: lista harmonicznych.
print("Zadanie 2 - FFT")

def fft(a):
    n = len(a)
    if n == 1:
        return a

    a_parzy = fft(a[::2])
    a_nieparzy = fft(a[1::2])

    w = np.exp(-2j * np.pi / n)
    w_i = 1
    y = [0] * n

    for i in range(n // 2):
        y[i] = a_parzy[i] + w_i * a_nieparzy[i]
        y[i + n // 2] = a_parzy[i] - w_i * a_nieparzy[i]
        w_i *= w

    return y

def zadanie2():
    values = list(map(float, input("Podaj próbki sygnału (oddzielone spacją) Pamiętaj - długość to potęga 2: ").split()))

    if not (len(values) and (len(values) & (len(values) - 1)) == 0):
        print("BŁĄD: Pamiętaj, że długość sygnału musi być potęgą dwójki!")
        return

    transformed = fft(values)
    print("Wynik FFT:")
    for i, val in enumerate(transformed):
        print(f"f[{i}] = {val:.3f}")

if __name__ == "__main__":
    zadanie2()

# Zadanie nr 3 – szybkie mnożenie wielomianów
# Zaimplementuj szybką procedurę mnożenia wielomianów reprezentowanych przez współczynniki (wykorzystaj FFT)
# Porównaj z naiwnym mnożeniem z zadania nr 1.
# Wejście: dwie listy współczynników wielomianu.
# Wyjście: lista współczynników wielomianu.
print("Zad 3 - szybkie mnożenie wielomianów")

def ifft(a):
    n = len(a)
    a_conj = np.conj(a)
    y = fft(a_conj)
    return np.conj(y) / n

def mnozenie_wielomianow_fft(A, B):
    n = 1
    while n < len(A) + len(B) - 1:
        n *= 2

    A_pad = A + [0] * (n - len(A))
    B_pad = B + [0] * (n - len(B))

    A_fft = fft(A_pad)
    B_fft = fft(B_pad)

    C_fft = [A_fft[i] * B_fft[i] for i in range(n)]
    C = ifft(C_fft)
    return [round(c.real) for c in C]

def zadanie3():
    A = list(map(float, input("Podaj współczynniki pierwszego wielomianu (oddzielone spacją): ").split()))
    B = list(map(float, input("Podaj współczynniki drugiego wielomianu (oddzielone spacją): ").split()))

    result = mnozenie_wielomianow_fft(A, B)
    print("Wynik - lista współczynnikó wielomianu:", result)

# porównanie wyniku z zad 1 i zad 3
    wynik_nawiny = naiwne_mnozenie_wielomianow(A, B)
    wynik_fft =mnozenie_wielomianow_fft(A, B)

    print("Wynik z algorytmu naiwnego:")
    print(wynik_nawiny)

    print("Wynik z algorytmu FFT:")
    print(wynik_fft)

    if wynik_nawiny == wynik_fft:
        print(" Oba wyniki są identyczne.")
    else:
        print(" Wyniki są różne.")

if __name__ == "__main__":
    zadanie3()

# Zadanie nr 4 – zestawienie
# Eksperymentalnie zbadaj szybkość obu procedur mnożenia dla rosnącego stopnia wielomianu. Wyniki przed-
# staw na wykresach czasu działania algorytmów od rozmiaru wielomianu.
# Wynik: wykresy czasu działania obu algorytmów od rozmiaru wielomianu.

print("Zadanie 4 - wykres")

import time
import matplotlib.pyplot as plt

def zadanie4():
    sizes = [2**i for i in range(4, 13)]
    times_naive = []
    times_fft = []

    for size in sizes:
        A = np.random.rand(size).tolist()
        B = np.random.rand(size).tolist()

        start = time.time()
        naiwne_mnozenie_wielomianow(A, B)
        times_naive.append(time.time() - start)

        start = time.time()
        mnozenie_wielomianow_fft(A, B)
        times_fft.append(time.time() - start)

        print(f"Rozmiar {size}: Naiwny = {times_naive[-1]:.6f}s, FFT = {times_fft[-1]:.6f}s")

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times_naive, label='Naiwne mnożenie', marker='o')
    plt.plot(sizes, times_fft, label='Mnożenie FFT', marker='x')
    plt.xlabel("Rozmiar wielomianu")
    plt.ylabel("Czas działania (s)")
    plt.title("Porównanie czasu mnożenia: naiwnego vs FFT")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    zadanie4()

# Zadanie nr 5 – filtrowanie sygnału
# Wykorzystaj FFT do filtracji zadanego sygnału okresowego – tzn. usunięcia wybranych częstotliwości.
# Niech dany będzie sygnał o postaci ∑ Ai sin(ai t) + ∑ Bj cos(bj t)
# Wejście: lista współczynników Ai, ai, Bj , bj . Parametry próbkowania.
# Wyjście: wykresy częstotliwości i sygnałów przed i po filtracji

print("Zadanie 5 - filtrowanie sygnału")

def generuj_sygnal(Ai, ai, Bj, bj, t):
    signal = np.zeros_like(t)
    for A, a in zip(Ai, ai):
        signal += A * np.sin(a * t)
    for B, b in zip(Bj, bj):
        signal += B * np.cos(b * t)
    return signal

def zadanie5():
    Ai = list(map(float, input("Podaj współczynniki Ai (oddzielone spacją): ").split()))
    ai = list(map(float, input("Podaj częstotliwości ai (oddzielone spacją): ").split()))
    Bj = list(map(float, input("Podaj współczynniki Bj (oddzielone spacją): ").split()))
    bj = list(map(float, input("Podaj częstotliwości bj (oddzielone spacją): ").split()))

    fs = int(input("Podaj częstotliwość próbkowania (przykładowo 1000): "))
    T = float(input("Podaj długość sygnału w sekundach (przykładowo 1.0): "))

    N = int(fs * T)
    t = np.linspace(0, T, N, endpoint=False)

    signal =  generuj_sygnal(Ai, ai, Bj, bj, t)

    freq = np.fft.fftfreq(N, d=1/fs) # FFT
    spectrum = np.fft.fft(signal)

    plt.figure(figsize=(12, 6))
    plt.subplot(2, 2, 1)
    plt.plot(t, signal)
    plt.title("Oryginalny sygnał")

    plt.subplot(2, 2, 2)
    plt.plot(freq[:N//2], np.abs(spectrum)[:N//2])
    plt.title("Widmo oryginalnego sygnału")

    do_usuniecia = list(map(float, input("Podaj częstotliwości do usunięcia (oddzielone spacją): ").split()))
    threshold = 1.0

    for r in do_usuniecia:
        indices = np.where((np.abs(freq - r) < threshold) | (np.abs(freq + r) < threshold))[0]
        spectrum[indices] = 0

    sfiltrowany_sygnal = np.fft.ifft(spectrum).real # IFFT

# po filtracji:

    plt.subplot(2, 2, 3)
    plt.plot(t, sfiltrowany_sygnal, color='magenta')
    plt.title("Sygnał po filtracji")

    plt.subplot(2, 2, 4)
    plt.plot(freq[:N//2], np.abs(spectrum)[:N//2])
    plt.title("Widmo po filtracji", color='magenta')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    zadanie5()