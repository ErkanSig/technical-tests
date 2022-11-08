import random
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

# print(bag)

def score4word(word):
    score = 0
    for letter in word:
        value = tile_values[letter]
        score += value
    return score

# print(score4word('GUARDIAN'))

def take_from_bag():
    rack = random.sample(bag, 7)
    for letter in rack:
        bag.remove(letter)
    return rack

rack = take_from_bag()

print(rack)
print(bag)


# Create every combination of 7 characters from rack
def letter_combinations(rack):
    words = []
    for i in range(len(rack)):
        words.append(rack[i])
        for j in range(1,len(rack)):
            if( i != j):
                words.append(F'{rack[i]}{rack[j]}')
            for k in range(2,len(rack)):
                if(i != k):
                    words.append(F'{rack[i]}{rack[j]}{rack[k]}')
                for l in range(3,len(rack)):
                    if(i != l):
                        words.append(F'{rack[i]}{rack[j]}{rack[k]}{rack[l]}')
                    for m in range(4,len(rack)):
                        if(i != m):
                            words.append(F'{rack[i]}{rack[j]}{rack[k]}{rack[l]}{rack[m]}')
                        for n in range(5,len(rack)):
                            if(i != n):
                                words.append(F'{rack[i]}{rack[j]}{rack[k]}{rack[l]}{rack[m]}{rack[n]}')
                            for o in range(6,len(rack)):
                                if(i != o):
                                    words.append(F'{rack[i]}{rack[j]}{rack[k]}{rack[l]}{rack[m]}{rack[n]}{rack[o]}')
    return words

combinations = letter_combinations(rack)
print(combinations[0:100])

# Check whether combination is in dictionary, add combinations that are to list called valid_words
def  word_checker(combinations):
    valid_words = []
    for combo in combinations:
        if combo in dictionary:
            valid_words.append(combo)
    return valid_words

valid_words = word_checker(combinations)
print(valid_words)

# Score all valid words, add scores to dictionary where the word is the key and its value is its score called word_scores


# Find length of longest word in valid_words.

# Find highest value in word_scores, return key.



# def letter_combinations(rack):
#     words = []
#     for i in range(len(rack)):
#         words.append(rack[i])
#         for j in range(1,len(rack)):
#             # if(j == i):
#             #     continue
#             # else:
#             words.append(F'{rack[i]}{rack[j]}')
#             for k in range(len(rack)):
#                 if(k == i | k == j):
#                     continue
#                 else:
#                     words.append(F'{rack[i]}{rack[j]}{rack[k]}')
#                     for l in range(len(rack)):
#                         if(l == i| l == j | l == k):
#                             continue
#                         else:
#                             words.append(F'{rack[i]}{rack[j]}{rack[k]}{rack[l]}')
#                             for m in range(len(rack)):
#                                 if(m == i | m == j | m == k | m == l):
#                                     continue
#                                 else:
#                                     words.append(F'{rack[i]}{rack[j]}{rack[k]}{rack[l]}{rack[m]}')
#                                     for n in range(len(rack)):
#                                         if(n == i| n == j | n == k | n == l | n == m):
#                                             continue
#                                         else:
#                                             words.append(F'{rack[i]}{rack[j]}{rack[k]}{rack[l]}{rack[m]}{rack[n]}')
#                                             for o in range(len(rack)):
#                                                 if(o == i | o == j | o == k | o == l | o == m | o == n):
#                                                     continue
#                                                 else:
#                                                     words.append(F'{rack[i]}{rack[j]}{rack[k]}{rack[l]}{rack[m]}{rack[n]}{rack[o]}')
#     return words