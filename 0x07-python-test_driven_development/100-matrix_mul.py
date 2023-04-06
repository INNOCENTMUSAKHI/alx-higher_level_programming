#!/usr/bin/python3
"""
Contains the matrix_mul function
"""


def matrix_mul(m_a, m_b):
    # Validate m_a and m_b
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")


if any(not all(isinstance(element, (int, float)) for element in row) for row in m_a):
    raise TypeError("m_a should contain only integers or floats")
if any(not all(isinstance(element, (int, float)) for element in row) for row in m_b):
    raise TypeError("m_b should contain only integers or floats")
    num_cols_m_a = len(m_a[0])
if any(len(row) != num_cols_m_a for row in m_a):
    raise TypeError("each row of m_a must be of the same size")
    num_cols_m_b = len(m_b[0])
    if any(len(row) != num_cols_m_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    num_rows_m_a = len(m_a)
    num_rows_m_b = len(m_b)
    if num_cols_m_a != num_rows_m_b:
        raise ValueError("m_a and m_b can't be multiplied")

    # Multiply matrices
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
