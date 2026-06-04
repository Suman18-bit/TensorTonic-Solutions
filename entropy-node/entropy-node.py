import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    y = np.array(y)
    
    # If y is empty, entropy = 0
    if y.size == 0:
        return 0.0
    
    _, counts = np.unique(y, return_counts=True)
    p = counts / counts.sum()
    
    entropy = np.sum(p * np.log2(p + 1e-12))

    if entropy>0:
        return entropy
    elif entropy<0:
        return -entropy
 
