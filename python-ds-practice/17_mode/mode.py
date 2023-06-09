def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    num_count = {}
    for num in nums:
        num_count[num] = nums.count(num)
    highest_key = None
    highest_value = 0
    for num in num_count.keys():
        if num_count[num] > highest_value:
            highest_key = num
            highest_value = num_count[num]
    return highest_key

print(mode([1, 2, 1]))
print(mode([2, 2, 3, 3, 2]))