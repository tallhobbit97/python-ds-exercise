def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    total1 = 0
    total2 = 0
    idx1 = 0
    idx2 = len(matrix[0]) - 1
    for num in range(len(matrix[0])):
        total1 += matrix[idx1][idx1]
        idx1 += 1
    for num in range(len(matrix[0])):
        total2 += matrix[num][idx2]
        idx2 -= 1
    return total1 + total2
    

m1 = [
    [1,   2],
    [30, 40],
]

print(sum_up_diagonals(m1))

m2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(sum_up_diagonals(m2))