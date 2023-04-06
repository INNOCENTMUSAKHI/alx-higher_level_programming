#!/usr/bin/python3
"""
Contains the matrix_mul function
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices(lists of lists of integers/floats)"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    num_rows_m_a = len(m_a)
    if num_rows_m_a == 0:
        raise ValueError("m_a can't be empty")
    num_cols_m_a = None
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
        if num_cols_m_a is None:
            num_cols_m_a = len(row)
            if num_cols_m_a == 0:
                raise ValueError("m_a can't be empty")
        if num_cols_m_a != len(row):
            raise TypeError("each row of m_a must should be of the same size")
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError("m_a should contain only integers or floats")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    num_rows_m_b = len(m_b)
    if num_rows_m_b == 0:
        raise ValueError("m_b can't be empty")
    num_cols_m_b = None
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")
        if num_cols_m_b is None:
            num_cols_m_b = len(row)
            if num_cols_m_b == 0:
                raise ValueError("m_b can't be empty")
        if num_cols_m_b != len(row):
            raise TypeError("each row of m_b must should be of the same size")
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if num_cols_m_a != num_rows_m_b:
        raise ValueError("m_a and m_b can't be multiplied")
    result_matrix = []
    for i in range(num_rows_m_a):
        result_row = []
        for j in range(num_cols_m_b):
            element_sum = 0
            for k in range(num_cols_m_a):
                element_sum += m_a[i][k] * m_b[k][j]
            result_row.append(element_sum)
        result_matrix.append(result_row)
    return result_matrix
