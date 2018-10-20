import vector
import math
EPSILON = 1e-3

def format_float(f):
    if abs(f) < EPSILON:
        return "0" 
    return ("%.3f" % f).rstrip('0').rstrip('.')

def format_complex(c):
    has_real = abs(c.real) > EPSILON
    has_imaginary = abs(c.imag) > EPSILON
    if not (has_real or has_imaginary):
        return "0"
    complex_string = ""
    if has_real:
        complex_string += format_float(c.real)
    if has_real and has_imaginary:
        complex_string += " + "
    if has_imaginary:
        coefficient = format_float(c.imag)
        if coefficient == "1":
            complex_string += 'i'
        elif coefficient == "-1":
            complex_string += '-i'
        else:
            complex_string += '{0}i'.format(coefficient)
        
    return complex_string

def pretty_print(matrix):
    row_space = range(len(matrix[0]))
    col_space = range(len(matrix))
    for r in row_space:
        row_string = "| "
        for c in col_space:
            entry = matrix[c][r]
            formatted = ""
            if isinstance(entry, complex):
                formatted = format_complex(entry)
            else:
                formatted = format_float(entry)
            padding = 18 - len(formatted)
            formatted += (" " * padding)
            row_string += formatted
        row_string += "|"
        print row_string

def scalar_mult(s, matrix):
    return [[r * s for r in c] for c in matrix]

def multiply(a, b):
    if len(a) != len(b[0]):
        raise Exception("column space of a does not equal dimension of row space of b")
    a_row_space = range(len(a[0]))
    b_col_space = range(len(b))
    new_matrix = [[0] * len(b) for _ in a_row_space]
    for i, b_col_vec in enumerate(b):
        for j in a_row_space:
            a_row_vec = [c[j] for c in a]
            new_matrix[i][j] = vector.inner_product(b_col_vec, a_row_vec)
    return new_matrix

        