#!/usr/bin/python3
""" Roman to Integer module """


def roman_to_int(roman_string):
    """ Converts a Roman numeral to an integer """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    rd = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    n = len(roman_string)

    for i in range(n):
        curr = rd.get(roman_string[i], 0)
        if i + 1 < n and rd.get(roman_string[i + 1], 0) > curr:
            res -= curr
        else:
            res += curr
    return res
