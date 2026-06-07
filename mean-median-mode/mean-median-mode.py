import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    x=np.array(x)
    mean = np.mean(x)
    median = np.median(x)
    counts = Counter(x)
    max_count = max(counts.values())
    mode = min(val for val, freq in counts.items() if freq == max_count)
    return mean , median , mode