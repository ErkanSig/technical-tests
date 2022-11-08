dictionary =  open('dictionary.txt', 'r').read()
# print(dictionary)

tile_values = {1: ['E', 'A', 'I', 'O', 'N', 'R', 'T', 'L', 'S', 'U'],
2: ['D', 'G'],
3: ['B', 'C', 'M', 'P'],
4: ['F', 'H', 'V', 'W', 'Y'],
5: 'K',
8: ['J', 'X'],
10: ['Q', 'Z']}

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

