def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = 'aeiou'
    lower_phrase = phrase.lower()
    vowels_freq = {}

    for char in lower_phrase:
        if vowels.find(char) > -1:
            if char in vowels_freq:
                vowels_freq[char] += 1
            else:
                vowels_freq[char] = 1
    return vowels_freq

print(vowel_count('rithm school'))
print(vowel_count('HOW ARE YOU? i am great!'))