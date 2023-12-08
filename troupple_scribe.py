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
    # Open the file and store the lines as a str list
    with open(path, 'r') as file:
        lines = file.readlines()

    # Stores the deck dictionary key and value (entry name and description) temprorarily
    current_elements = ['', '']
    # Regex pattern for finding the key (entry name)
    key_pattern = re.compile('.+?(?=\t)')
    # Regex pattern for finding the value (description)
    value_pattern = re.compile('(?<=\t)(.*?)(?=\[)')
    # set_pattern = re.compile('(?<=\[)(.*?)(?=\])')

    # On every line...
    for line in lines:
        # Find the key (entry name) by looking for everything before a tab
        # Store it to the temp array
        current_elements[0] = re.search(key_pattern, line).group()
        # Find the value (description) by looking for everything in between a tab and '['
        # (set name is in [])
        # Store it to the temp array
        current_elements[1] = re.search(value_pattern, line).group()

        # If red deck
        if color == True:
            # Populate red deck
            red[current_elements[0]] = current_elements[1]
        # Otherwise it's green
        else:
            green[current_elements[0]] = current_elements[1]


# Populate red deck
populate_deck('data/red.txt', True)
# Populate green deck
populate_deck('data/green.txt', False)

# Find a random key value pair from the red deck dictionary
# dict.items() returns a special object, so it needs to be casted to an ordered data struct
# random.sample() return a list of tuples, so I simply it to store the first element
red_result = random.sample(list(red.items()), 1)[0]
# Find a random key value pair from the green deck dictionary
green_result = random.sample(list(green.items()), 1)[0]

# Print results in the format:
# <Entry name>: <description>
# with a new line in between
print(f'{red_result[0]}: {red_result[1]}')
print(f'{green_result[0]}: {green_result[1]}')
