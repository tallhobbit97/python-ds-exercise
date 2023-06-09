def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    str1 = str(num1)
    str2 = str(num2)
    dict1 = {}
    dict2 = {}
    for char in str1:
        if char in dict1:
            dict1[char] += 1
        else:
            dict1[char] = 1
    for char in str2:
        if char in dict2:
            dict2[char] += 1
        else:
            dict2[char] = 1
    if dict1 == dict2:
        return True
    else:
        return False

print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
print(same_frequency(1212, 2211))