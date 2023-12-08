import random
import re

# SETS = [
#     'Core Set',
#     'Core Expansion 1',
#     'Core Expansion 2',
#     'Core Expansion 3',
#     'Core Expansion 4',
#     'Party Box',
#     'Party Box Expansion 1',
# ]

# Dictionaries representing the decks
# Format: entry name → description
red = {}
green = {}

# path (str): path to data file
# color (bool): True = red deck, False = green deck
# return type: None
# Populates a deck dict
def populate_deck(path: str, color: bool) -> None:
    lines = []
    with open(path, 'r') as file:
        lines = file.readlines()

    current_elements = ['', '']
    key_pattern = re.compile('.+?(?=\t)')
    value_pattern = re.compile('(?<=\t)(.*?)(?=\[)')
    # set_pattern = re.compile('(?<=\[)(.*?)(?=\])')

    for line in lines:
        current_elements[0] = re.search(key_pattern, line).group()
        current_elements[1] = re.search(value_pattern, line).group()

        if color == True:
            red[current_elements[0]] = current_elements[1]
        else:
            green[current_elements[0]] = current_elements[1]


populate_deck('data/red.txt', True)
populate_deck('data/green.txt', False)

red_result = random.sample(list(red.items()), 1)[0]
green_result = random.sample(list(green.items()), 1)[0]

print(f'{red_result[0]}: {red_result[1]}')
print(f'{green_result[0]}: {green_result[1]}')
