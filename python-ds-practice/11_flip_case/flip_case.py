def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    lower_swap = to_swap.lower()
    uppper_swap = to_swap.upper()
    new_string = []
    for char in phrase:
        if char == lower_swap:
            new_string.append(char.upper())
        elif char == uppper_swap:
            new_string.append(char.lower())
        else:
            new_string.append(char)
    return ''.join(new_string)

print(flip_case('Aaaaaahhh', 'a'))
print(flip_case('Aaaaaahhh', 'A'))
print(flip_case('Aaaaaahhh', 'h'))