import math
import matrix
import cmath

identity = [[1, 0], [0, 1]]

hadamard = matrix.scalar_mult(1/math.sqrt(2),[[1, 1], [1, -1]])
def r_z(theta):
    return [
        [cmath.exp((-theta/2) * 1j), 0],
        [0, cmath.exp((theta/2) * 1j)]
    ]

def r_x(theta):
    return [
        [math.cos(theta/2), -1j * math.sin(theta/2)],
        [-1j * math.sin(theta/2), math.cos(theta/2)]
    ]

def r_y(theta):
    return [
        [math.cos(theta/2), math.sin(theta/2)],
        [-math.sin(theta/2), math.cos(theta/2)]
    ]

def r(n, theta):
    return [
        [math.cos(theta/2) - 1j * math.sin(theta/2) * n[2], 
        -1j * math.sin(theta/2) * (n[0] + 1j*n[1])],
        [-1j * math.sin(theta/2) * (n[0] - 1j*n[1]),
        math.cos(theta/2) + 1j * math.sin(theta/2) * n[2]]
    ]