"""
Write a function that takes in a non-empty array of integers that are sorted
in ascending order and returns a new array of the same length with the squares
of the original integers also sorted in ascending order.
Sample Input:
array = [1, 2, 3, 5, 6, 8, 9]
Sample output:
[1, 4, 9, 25, 36, 64, 81]
Some constrains that candidate should be aware of:
- are the array elements unique? (yes)
- are there negative numbers? (yes)
- the minimum and maximum size of the input array (1 to 2^31 - 1)
- can I modify the original array? (no)
"""
from ast import And


def squares(*numbers):
    """
    Computes and returns the squares (sorted) for the given numbers.
    >>> squares(1, 2, 3, 5, 6, 8, 9)
    [1, 4, 9, 25, 36, 64, 81]
    >>> squares(-10, -3, -2, 2, 5, 9)
    [4, 4, 9, 25, 81, 100]
    """
    s_array= [item**2 for item in numbers]
    if s_array[0]>s_array[1]:
        n = len(s_array)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if s_array[j] > s_array[j + 1] :
                    s_array[j], s_array[j + 1] = s_array[j + 1], s_array[j]  

    return s_array