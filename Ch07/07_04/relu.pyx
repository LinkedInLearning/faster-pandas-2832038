#cython: language_level=3

def relu(double n):
    if n < 0:
        return 0
    return n
