# Projektowanie algorytmów 2 Oliwia Borkowska

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

# zadanie 1
print("ZADANIE 1")
class AutomatSkonczony:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3'}
        self.alphabet = {'0', '1'}
        self.transitions = {
            'q0': {'0': 'q1', '1': 'q0'},
            'q1': {'0': 'q3', '1': 'q2'},
            'q2': {'0': 'q2', '1': 'q0'},
            'q3': {'0': 'q2', '1': 'q2'}
        }
        self.start_state = 'q0'
        self.accept_states = {'q3'}

    def wprowadzanie(self, input_string):
        state = self.start_state
        print(f"Start: {state}")
        for symbol in input_string:
            if symbol not in self.alphabet:
                print(f"Symbol '{symbol}' jest nieprawidłowy")
                return
            state = self.transitions[state][symbol]
            print(f" -> {state}")

        if state in self.accept_states:
            print(f"Wejście zostało zaakceptowane w stanie {state}")
        else:
            print(f"Wejście zostało odrzucone w stanie {state}.")

input_data = input("Podaj ciąg wejściowy - składający się wyłącznie z 0 i 1: ")
fsm =AutomatSkonczony() #finite-state machine (fsa)
fsm.wprowadzanie(input_data)

# zadanie 2 (z rysunkiem)
print("ZADANIE 2")


class AutomatSkonczony_nr2:
    def __init__(self):
        self.states = {"q0", "q1", "q2", "q3", "q4", "q5", "q6"}
        self.alphabet = {"a", "b", "c"}
        self.transition_function = {
            "q0": {"a": "q2", "b": "q2", "c": "q2"},
            "q1": {"a": "q4", "b": "q0", "c": "q3"},
            "q2": {"a": "q1", "b": "q1", "c": "q6"},
            "q3": {"a": "q3", "b": "q3", "c": "q3"},
            "q4": {"a": "q0", "b": "q5", "c": "q5"},
            "q5": {"a": "q4", "b": "q4", "c": "q4"},
            "q6": {"a": "q3", "b": "q3", "c": "q3"},
        }
        self.start_state = "q0"
        self.accept_states = {"q0", "q4", "q5"}
        self.graph = nx.DiGraph()
        self. budowa_grafu()

    def budowa_grafu(self):
        edge_labels = defaultdict(set)
        for state, edges in self.transition_function.items():
            for symbol, next_state in edges.items():
                edge_labels[(state, next_state)].add(symbol)

        for (start, end), symbols in edge_labels.items():
            self.graph.add_edge(start, end, label=",".join(symbols))

    def wejscie(self, input_string2):
        current_state = self.start_state
        path = [current_state]
        print(f"Start: {current_state}")

        for symbol in input_string2:
            if symbol not in self.alphabet:
                print(f"Symbol '{symbol}' jest nieprawidłowy")
                return
            next_state = self.transition_function[current_state][symbol]
            print(f"{current_state} --- {symbol} ---> {next_state}")
            current_state = next_state
            path.append(current_state)

        if current_state in self.accept_states:
            print(f"Zakończono w stanie akceptującym: {current_state}")
        else:
            print(f"Zakończono w stanie nieakceptującym: {current_state}")

        self.rysowanie_grafu(path)

    def rysowanie_grafu(self, path):
        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(self.graph)
        labels = nx.get_edge_attributes(self.graph, 'label')

        node_colors = ["magenta" if state == self.start_state else "pink" for state in self.graph.nodes()]
        node_edge_widths = [3 if state in self.accept_states else 1 for state in self.graph.nodes()]

        nx.draw(self.graph, pos, with_labels=True, node_size=2500, node_color=node_colors, edgecolors='black',
                linewidths=node_edge_widths, font_size=10, font_weight='bold')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)

        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(self.graph, pos, edgelist=path_edges, edge_color='violet', width=3, alpha=0.7)
        plt.show()



input_string2 = input("Podaj ciąg wejściowy - składający się wyłącznie z liter: a, b i c: ")
print("Ciąg wejściowy:", input_string2)
fsm2 = AutomatSkonczony_nr2()
fsm2.wejscie(input_string2)


# zadanie 3  Napisz program (niekoniecznie automat skończony) rozpoznający język A = {auaw : u,w ∈ {0,1}∗}.
#  Wejście: ciąg wejściowy automatu.
#  Wyjście: informacja: język rozpoznany, język nierozpoznany.
print("ZADANIE 3")

# z polecenia rozumiem, że ciąg musi zaczynać się od litery a, posiadać jeszcze jedną literę a w sobie,
# natomiast w środku mają znajdować się liczby 0 oraz 1


def rozpoznawanie_jezyka(ciag):
    if len(ciag) < 2:
        return "Nie można rozpowznać języka. Ciąg zbyt krótki."

    if ciag[0] == "a" and "a" in ciag[1:]:
        return "Rozpoznano język."
    return "Nie rozpoznano języka."


ciag_wejsciowy = input("Podaj ciąg wejściowy składający się z conamniej dwóch liter a i dodatkowo z 0 i 1: ")
wynik = rozpoznawanie_jezyka(ciag_wejsciowy)
print(wynik)

# zadanie 4  Napisz program symulujący automat rozpoznający język B = {anbcdm : n ≥ 0,m ≥ 0}.
# Przedstaw symulację dla zadanego ciągu wejściowego.
#  Wejście: ciąg wejściowy automatu.
#  Wyjście: symulacja działania automatu (w konsoli).
print("ZADANIE 4")


def jezyka_rozpoznawanie(ciag1):
    state = "q0"  # Stan początkowy
    index = 0

    print(f"Wejściowy ciąg: {ciag1}")

    while index < len(ciag1):
        char = ciag1[index]
        print(f"Stan: {state}, przetwarzany znak to: {char}")

        if state == "q0":
            if char == 'a':
                state = "q0"
            elif char == 'b':
                state = "q1"
            else:
                print("Błąd, zły znak")
                return False

        elif state == "q1":
            if char == 'c':
                state = "q2"
            else:
                print("Błąd, należało wprowadzić: 'c'")
                return False

        elif state == "q2":
            if char == 'd':
                state = "q3"
            else:
                print("Błąd, należało wprowadzić: 'd'")
                return False

        elif state == "q3":
            if char == 'd':
                state = "q3"
            else:
                print("Błąd, nie można wprowadzić znaku po 'd'")
                return False

        index += 1

    if state == "q3":
        print("Ciąg zaakceptowany.")
        return True
    else:
        print("Ciąg odrzucony.")
        return False

ciag1 = input("Podaj ciąg wejściowy składający się z liter a,b,c,d: ")
jezyka_rozpoznawanie(ciag1)

# zadanie 5
print("ZADANIE 5")
import json

def load_automaton(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def simulate_automaton(automaton, input_string):
    state = automaton["start_state"]
    print(f"Wejściowy ciąg: {input_string}")

    for char in input_string:
        print(f"Stan: {state}, przetwarzany znak: {char}")
        if char in automaton["transitions"].get(state, {}):
            state = automaton["transitions"][state][char]
        else:
            print("Błąd: Niedozwolony znak lub brak przejścia!")
            return False

    if state in automaton["accept_states"]:
        print("Ciąg zaakceptowany!")
        return True
    else:
        print("Ciąg odrzucony!")
        return False

# utworzenie pliku JSON dla automatu z zadania nr 4
automaton_data = {
    "states": ["q0", "q1", "q2", "q3"],
    "alphabet": ["a", "b", "c", "d"],
    "transitions": {
        "q0": {"a": "q0", "b": "q1"},
        "q1": {"c": "q2"},
        "q2": {"d": "q3"},
        "q3": {"d": "q3"}
    },
    "start_state": "q0",
    "accept_states": ["q3"]
}

# zapis do pliku JSON
json_filename = "automat_zad4.json"
with open(json_filename, 'w') as json_file:
    json.dump(automaton_data, json_file, indent=4)

print(f"Zapisano automat do pliku {json_filename}")

file_path = input("Podaj ścieżkę do pliku JSON z automatem (automat_zad4.json): ")
automaton = load_automaton(file_path)
input_string = input("Podaj ciąg wejściowy składający się z liter a, b, c, d: ")
simulate_automaton(automaton, input_string)
