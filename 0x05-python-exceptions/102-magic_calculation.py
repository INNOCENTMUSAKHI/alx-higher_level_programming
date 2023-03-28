#!/usr/bin/python3
# 102-magic_calculation.py
# Brennan D Baraban <375@holbertonschool.com>


def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise ValueError('Too far')
            result += a ** b / i
        except ZeroDivisionError:
            return "division by zero"
        except Exception as e:
            result = b + a
    return result
