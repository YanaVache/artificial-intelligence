"""
Ten kod rozwiązuje zadanie polegające na obliczeniu minimalnej liczby operacji zamiany bitu, 
która da jeden ciąg jedynek o zadanej długości D otoczony zerami dla danego ciągu bitów (0/1). 
Funkcja opt_dist używa techniki przesuwającego się okna do analizy podciągów o długości D 
w ciągu bitów i obliczenia minimalnej liczby operacji potrzebnych do utworzenia ciągu o długości D 
składającego się tylko z jedynek. Funkcja ta jest wykorzystywana w pętli wejścia, która czyta dane 
z pliku wejściowego, przetwarza je za pomocą funkcji opt_dist i zapisuje wyniki do pliku wyjściowego."""
import math

def opt_dist(ciag, D):
    """
    :param ciag: lista 0/1
    :param D: długość oczekiwanego ciągu jedynek
    :return: minimalna liczba zamian bitów potrzebna do uzyskania ciągu o długości D (pozostałe są zerami)
    """
    n = len(ciag)
    ile_jedynek = sum(bit == '1' for bit in ciag)

    min_moves = ile_jedynek + D  # zamiana wszystkich jedynek na zera, aby otrzymać ciąg o długości D składający się tylko z jedynek

    # używamy techniki przesuwania okna (o długości D)
    for i in range(0, n - D + 1):
        ile_jedynek_okno = 0  # liczba jedynek w oknie

        for j in range(i, i + D):
            if ciag[j] == '1':
                ile_jedynek_okno += 1
        do_zamiany_zew = ile_jedynek - ile_jedynek_okno  # liczba jedynek do zamiany na zera poza oknem
        do_zamiany_wew = D - ile_jedynek_okno           # liczba zer do zamiany na jedynki wewnątrz okna

        if do_zamiany_wew + do_zamiany_zew < min_moves:
            min_moves = do_zamiany_wew + do_zamiany_zew

    return min_moves


# Wczytywanie danych z pliku i przekazanie ich do funkcji opt_dist
def input_handler():
    with open("zad4_input.txt", "r") as rd:
        with open("zad4_output.txt", "w") as wr:
            for line in rd:
                line = line.split()
                print(opt_dist(line[0], int(line[1])), file=wr)


input_handler()


