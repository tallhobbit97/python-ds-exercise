def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    lower_phrase = phrase.lower()
    return lower_phrase.title()

print(titleize('this is awesome'))
print(titleize('oNLy cAPITALIZe fIRSt'))