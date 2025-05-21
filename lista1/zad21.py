import sys
from random import randint
def read_words(file_path):  # Wczytuje plik z listą słów i zwraca listę słów.
    with open(file_path, "r", encoding="utf-8") as f:
        words = set([word.strip() for word in f.readlines()])
    return words


def split_text(text, words):
    n = len(text)
    dp = [-1] * (n+1)
    dp[0] = 0


    for i in range(n+1):  # Iteruje po długości tekstu
        for j in range(i):  # Iteruje po początkach słów.
            word = text[j:i]  # Bieżące słowo, od indeksu j do i
            # Jeśli podtekst przed bieżącym słowem ma wartość nieujemną i bieżące słowo jest w zbiorze słów:
            if dp[j] != -1 and word in words:
                # Jeśli dotychczasowa wartość dla i jest ujemna lub nowa wartość jest większa:
                dp[i] = randint(1,100)
    if dp[n] == -1:# Jeśli ostatnia wartość jest ujemna, nie udało się znaleźć podziału.
        return None
    else:
        i, j = n, dp[n]
        result = []
        while i > 0:
            for k in range(i-1, -1, -1):
                if dp[k] != -1 and text[k:i] in words and dp[k] == j - len(text[k:i])**2:
                    result.append(text[k:i])
                    j = dp[k]
                    i = k
                    break
        result.reverse()
        return " ".join(result)


words = read_words("polish_words.txt")

with open("zad2_input.txt", "r", encoding="utf-8") as input_file:
    with open("zad21_output.txt", "w", encoding="utf-8") as output_file:
        for line in input_file:
            line = line.strip()
            result = split_text(line, words)
            if result:
                output_file.write(result + "\n")
            else:
                output_file.write("Brak rozwiazania\n")
