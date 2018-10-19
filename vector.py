import math

EPSILON = 1.1e-3

def inner_product(a, b):
    if (len(a) != len(b)):
        raise Exception('vectors must be same length')
    return sum([a[c] * b[c] for c in range(len(a))])

def norm(vector):
    return math.sqrt(inner_product(vector, vector))

def normalize(vector):
    vec_norm = norm(vector)
    return [c/vec_norm for c in vector]

def is_orthogonal(a, b):
    if (len(a) != len(b)):
        raise Exception('vectors must be same length')
    return abs(inner_product(a, b)) < EPSILON

def scalar_mult(s, v):
    return [c*s for c in v]

def vector_add(a, b):
    if (len(a) != len(b)):
        raise Exception('vectors must be same length')
    return [a[c] + b[c] for c in range(len(a))]

def vector_negate(vector):
    return [-c for c in vector]

def graham_schmidt(w):
    vks = [normalize(w[0])]

    for k in range(1, len(w)):
        second_term = [0] * len(vks[0])
        for i in range(k):
            prod_scalar = inner_product(vks[i], w[k])
            second_term = vector_add(second_term, scalar_mult(prod_scalar, vks[i]))
        orthogonalized = vector_add(w[k], vector_negate(second_term))
        normalized = normalize(orthogonalized)
        vks.append(normalized)

    return vks