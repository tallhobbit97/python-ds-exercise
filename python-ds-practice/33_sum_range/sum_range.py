def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
    total = 0
    if start == 0 and end == None:
        for num in nums:
            total += nums[num - 1]
    if start == 0 and isinstance(end, int):
        for num in range(start, end + 1):
            total += nums[num]
    elif start > 0 and end == None:
        for num in range(start, len(nums)):
            total += nums[num]
    elif start > 0 and isinstance(end, int) and end > len(nums):
        for num in range(start, len(nums)):
            total += nums[num]
    elif start > 0 and isinstance(end, int) and end <= len(nums):
        for num in range(start, end + 1):
            total += nums[num]
    return total

nums = [1, 2, 3, 4]
print(sum_range(nums))
print(sum_range(nums, 1))
print(sum_range(nums, end=2))
print(sum_range(nums, 1, 3))
print(sum_range(nums, 1, 99))