"""
Provide classes to set game.
"""

# Full representation for properties of Set cards, in program they are always
# represented as either 0, 1 or 2, while their string representations are used
# for the user interface.
# To make inputting cards easier, key_symbols is a list of strings (mostly
# single characters) that can be looked for in the user input to identify cards.
# When trying to parse a card input, the program will look for every entry of
# key_symbols when searching for card properties.
PROP_REPR = {
    "amount": {
        0: {
            "string": "One",
            "key_symbols": ["1", "one"],
        },
        1: {
            "string": "Two",
            "key_symbols": ["2", "two"],
        },
        2: {
            "string": "Three",
            "key_symbols": ["3", "three"],
        },
    },
    "color": {
        0: {
            "string": "red",
            "key_symbols": ["r", "red"],
        },
        1: {
            "string": "green",
            "key_symbols": ["g", "green"],
        },
        2: {
            "string": "violet",
            "key_symbols": ["v", "violet"],
        },
    },
    "shape": {
        0: {
            "string": "oval",
            "key_symbols": ["o", "O", "0", "oval"],
        },
        1: {
            "string": "tilde",
            "key_symbols": ["t", "~", "tilde"],
        },
        2: {
            "string": "diamond",
            "key_symbols": ["d", "diamond"],
        },
    },
    "fill": {
        0: {
            "string": "empty",
            "key_symbols": ["e", "empty"],
        },
        1: {
            "string": "full",
            "key_symbols": ["f", "full"],
        },
        2: {
            "string": "hatched",
            "key_symbols": ["h", "hatched", "c", "cross"],
        },
    },
}

class SetBoard:
    """
    Represent a board of set cards.
    Contains methods to find sets, add or remove cards.
    """

    def __init__(self):
        pass

    def add_cards_by_user(self, amount: int = 1):
        for i in range(amount):
            pass
    
    def check_for_duplicates(self):
        pass

    def find_set(self):
        pass


class SetCard:
    """
    Represent a single Set card, which consists of four properties, each of
    which takes on exactly one of three values.
    """

    def __init__(self, description_string: str) -> None:

        # For every property name listed in PROP_REPR, get the sub dicts
        # with the values 0, 1 and 2 and match their respective key symbols
        # against the given string.
        # Stop if a match is found and set self.<name-of-that-property>
        # to the value in whose dict the matching key symbol was found.
        for property in PROP_REPR.keys():
            for value, info in PROP_REPR[property].items():
                if any(key_symbol in description_string for key_symbol in info["key_symbols"]):
                    self.__setattr__(property, value)
        
        # Check if a valid card description was given, meaning all four
        # properties could be assigned.
        
    
    def __repr__(self):

        # Join the string representations of all four property values together
        # separated by a whitespace, order is given by the order in which
        # they are listed in PROP_REPR.
        return " ".join([
            PROP_REPR[property][self.__getattribute__(property)]["string"]
            for property in PROP_REPR.keys()
        ])