import numpy as np
def manhattan_distance(p1, p2):
    return float(sum(abs(float(x) - float(y)) for x, y in zip(p1, p2)))
    