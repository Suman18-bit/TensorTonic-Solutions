import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x = np.array(x, dtype=float)
    p = np.array(p, dtype=float)
    
    # Safety check: probabilities must sum to 1
    if not np.isclose(np.sum(p), 1):
        raise ValueError("Probabilities must sum to 1.")
    
    # Expected value formula: sum(x * p)
    return np.sum(x * p)

    
    pass
