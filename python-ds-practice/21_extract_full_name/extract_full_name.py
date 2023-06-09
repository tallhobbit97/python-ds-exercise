def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    new_list = []
    for person in people:
        name = ' '.join(list(person.values()))
        new_list.append(name)
    return new_list

names = [
{'first': 'Ada', 'last': 'Lovelace'},
{'first': 'Grace', 'last': 'Hopper'},
]

print(extract_full_names(names))