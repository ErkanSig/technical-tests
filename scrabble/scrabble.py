dictionary =  open('dictionary.txt', 'r').read()
# print(dictionary)

tile_values = {'E': 1, 'A': 1, 'I': 1, 'O': 1, 'N': 1, 'R': 1, 'T': 1, 'L': 1, 'S': 1, 'U': 1,
'D': 2, 'G': 2,
'B': 3, 'C': 3, 'M': 3, 'P': 3,
'F':4, 'H':4, 'V':4, 'W':4, 'Y': 4,
'K': 5,
'J':8, 'X': 8,
'Q':10, 'Z': 10}

tile_distribution = {12: 'E',
9:	['A', 'I'],
8:	'O',
6:	['N', 'R', 'T'],
4:	['L', 'S', 'U', 'D'],
3:	'G',
2:	['B', 'C', 'M', 'P', 'F', 'H', 'V', 'W', 'Y'],
1:	['K', 'J', 'X', 'Q', 'Z']}

bag = []

for key, value in tile_distribution.items():
    for letter in value:
        for i in range(key):
            bag.append(letter)

print(bag)

def score4word(word):
    score = 0
    for letter in word:
        value = tile_values[letter]
        score += value
    return score

print(score4word('GUARDIAN'))