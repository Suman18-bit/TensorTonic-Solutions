import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    x : list or array-like
        Input data.
    q : list or array-like
        Percentile values in [0,100].
    Returns: array of percentile values.
    """
    
    x = np.array(x, dtype=float)
    q = np.array(q, dtype=float)
    x_sorted = np.sort(x)
    n = len(x_sorted)
    positions = (q / 100) * (n - 1)
    lower = np.floor(positions).astype(int)
    upper = np.ceil(positions).astype(int)
    frac = positions - lower
    result = (1 - frac) * x_sorted[lower] + frac * x_sorted[upper]

    return result
