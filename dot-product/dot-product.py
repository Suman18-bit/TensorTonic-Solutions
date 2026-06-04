import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    
    # Check shape compatibility
    if x.shape != y.shape:
        raise ValueError(f"Shape mismatch: {x.shape} vs {y.shape}. Arrays must have the same length.")
    
    return float(np.dot(x, y))


                    