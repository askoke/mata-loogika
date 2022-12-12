"""Dictionary exercises."""
import math

def get_hobbies(name: str) -> list:
    """
    Return the hobbies of a given person.

    hobbies = {
    "Tom": ["running", "reading"],
    "John": ["movies", "music", "swimming"]
    }

    get_hobbies(hobbies, "Tom")  => ["running", "reading"]
    get_hobbies(hobbies, "Timmy")  => "name not in dictionary"

    :param hobbies_dict: dictionary with peoples' hobbies.
    :param name: name of person whose hobbies are to be returned.

    :return: List of hobbies of the person with given name or "name not in dictionary".
    """
    if name in hobbies_dict.keys():
        return hobbies_dict.get(name)
    else:
        return "name not in dictionary"


def find_tallest(height_dict: dict) -> str:
    """
    Return the name of the tallest person in given dictionary.

    find_tallest({"Tom": 186, "Mari": 175, "Jhon": 190}) => "Jhon"

    :param height_dict: dictionary with peoples' names and heights
    :return: name of tallest person in given dict.
    """
    tallest = 0
    for i in height_dict.keys():
        if height_dict[i] > tallest:
            tallest = height_dict[i]
    for i in height_dict.keys():
        if height_dict[i] == tallest:
            return i


def remove_sixes(six_dict: dict) -> dict:
    """
    Return a dictionary where all keys which's values are dividable by six are removed.

    remove_sixes({"a": 4, "b": 8, "c": 6, "d": 18}) => {"a": 4, "b": 8}

    :param six_dict: dictionary to be modified.
    :return: dict without values that are dividable by six.
    """
    new_dict = {}
    for i in six_dict.keys():
        if (six_dict[i] % 6) == 0:
            new_dict[i] = six_dict[i]
            del new_dict[i]
        else:
            new_dict[i] = six_dict[i]
    return new_dict


def exchange_keys_and_values(exchange_dict: dict) -> dict:
    """
    Return a dict where keys and values have been exchanged.

    exchange_keys_and_values({"a": "b", "c": "d"}) => {"b": "a", "d": "c"}

    :param exchange_dict: dictionary to be modified.
    :return dictionary where values and keys have been exchanged.
    """
    new_dict = {}
    for i in exchange_dict.keys():
        new_dict[exchange_dict[i]] = i
    return new_dict


def count_symbol_appearances(stringy: str) -> dict:
    """
    Return dict where key is the symbol and the value is the count this symbol is present in the string.

    count_symbol_appearances("hello hi") => {'h': 2, 'e': 1, 'l': 2, 'o': 1, ' ': 1, 'i': 1}

    :param stringy: string to be processed.
    :return: dictionary with symbol counts.
    """
    new_dict = {}
    for i in stringy:
        if stringy.count(i) > 1:
            new_dict[i] = stringy.count(i)
        else:
            new_dict[i] = 1
    return new_dict


def organise_by_first_symbol(strings: list) -> dict:
    """
    Return dict where key the is a symbol and the value is a list of words starting with this symbol.

    organise_by_first_symbol(["hello", "word", "world", "welcome", "yes"]) =>
        {'h': ['hello'], 'w': ['word', 'world', 'welcome'], 'y': ['yes']}

    :param strings: list of strings.
    :return: dict with starting symbol and corresponding words in order of appearance.
    """
    new_dict = {}
    for i in strings:
        if i[0] not in new_dict:
            new_dict[i[0]] = [i]
        else:
            new_dict[i[0]].append(i)
    return new_dict