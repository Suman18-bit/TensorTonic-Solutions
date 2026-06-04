import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    point_x=np.array(x)
    point_y=np.array(y)
    
    distance = np.linalg.norm(point_x - point_y)
    return distance