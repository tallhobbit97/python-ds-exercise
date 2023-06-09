def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    status = None
    for item in lst:
        if isinstance(item, list):
            status = True
        else:
            status = False
    return status

print(list_check([[1], [2, 3]]))
print(list_check([[1], "nope"]))
