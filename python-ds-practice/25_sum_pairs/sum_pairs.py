def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    found = None
    nums_found = []
    # for num in nums:
    #     for num2 in nums:
    #         if num + num2 == goal:
    #             found = True
    #             nums_found.append(tuple([num, num2]))
    #             break
    for num in range(0, len(nums) - 1):
        if nums[num] > goal:
            nums.pop(num)

    for num in range(0, len(nums) - 1):
        if nums[num] + nums[num + 1] == goal:
            found = True
            nums_found.append(tuple([nums[num], nums[num+1]]))
            break
    if found:
        return nums_found[0]
    else:
        return ()

print(sum_pairs([1, 2, 2, 10], 4))
print(sum_pairs([4, 2, 10, 5, 1], 6))
print(sum_pairs([5, 1, 4, 8, 3, 2], 7))
print(sum_pairs([11, 20, 4, 2, 1, 5], 100))