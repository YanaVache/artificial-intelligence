import random
from itertools import combinations

# pierwszy index to karta, drugi to kolor

# TALIE
playerFig = [
            [0,0], [0,1], [0,2], [0,3],
            [1,0], [1,1], [1,2], [1,3],
            [2,0], [2,1], [2,2], [2,3],
            [3,0], [3,1], [3,2], [3,3]
        ]

playerBlo = [
            [0,0], [0,1], [0,2], [0,3],
            [1,0], [1,1], [1,2], [1,3],
            [2,0], [2,1], [2,2], [2,3],
            [3,0], [3,1], [3,2], [3,3],
            [4,0], [4,1], [4,2], [4,3],
            [5,0], [5,1], [5,2], [5,3],
            [6,0], [6,1], [6,2], [6,3],
            [7,0], [7,1], [7,2], [7,3],
            [8,0], [8,1], [8,2], [8,3]
        ]

figScore = [0, 0, 0, 0, 0, 0, 0, 0, 0]
bloScore = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# Poker - 8, Kareta - 7, ..., Para - 1, Karta - 0
def calcHandScore(hand):
    if hand[0][0]+1 == hand[1][0] and hand[1][0]+1 == hand[2][0] and hand[2][0]+1 == hand[3][0] and hand[3][0]+1 == hand[4][0]:
        if hand[0][1] == hand[1][1] and hand[1][1] == hand[2][1] and hand[2][1] == hand[3][1] and hand[3][1] == hand[4][1]:
            return 8
    if hand[0][0] == hand[1][0] and hand[1][0] == hand[2][0] and hand[2][0] == hand[3][0] or hand[1][0] == hand[2][0] and hand[2][0] == hand[3][0] and hand[3][0] == hand[4][0]:
        return 7
    if hand[0][0] == hand[1][0] and hand[1][0] == hand[2][0] and hand[3][0] == hand[4][0] or hand[0][0] == hand[1][0] and hand[2][0] == hand[3][0] and hand[3][0] == hand[4][0]:
        return 6
    if hand[0][1] == hand[1][1] and hand[1][1] == hand[2][1] and hand[2][1] == hand[3][1] and hand[3][1] == hand[4][1]:
        return 5
    if hand[0][0]+1 == hand[1][0] and hand[1][0]+1 == hand[2][0] and hand[2][0]+1 == hand[3][0] and hand[3][0]+1 == hand[4][0]:
        return 4
    if hand[0][0] == hand[1][0] and hand[1][0] == hand[2][0] or hand[2][0] == hand[3][0] and hand[3][0] == hand[4][0]:
        return 3
    if hand[0][0] == hand[1][0] and hand[2][0] == hand[3][0] or hand[0][0] == hand[1][0] and hand[3][0] == hand[4][0] or hand[1][0] == hand[2][0] and hand[3][0] == hand[4][0]:
        return 2
    if hand[0][0] == hand[1][0] or hand[1][0] == hand[2][0] or hand[2][0] == hand[3][0] or hand[3][0] == hand[4][0]:
        return 1
    return 0

def genAllBlotkarzHands():
    return list( combinations( playerBlo, 5 ))

def genAllFigurantHands():
    return list( combinations( playerFig, 5 ))

def getData():
    blo = genAllBlotkarzHands()
    for b in blo:
        bloScore[calcHandScore(b)] += 1
    fig = genAllFigurantHands()
    for f in fig:
        figScore[calcHandScore(f)] += 1
    bloWins = 0.0
    games = 0.0

    for fidx, fs in enumerate(figScore):
        for bidx, bs in enumerate(bloScore):
            if(bidx > fidx):
                bloWins += fs * bs
            games += fs * bs

    print(str(round(bloWins / games * 100, 3)) + "%")

getData()

    