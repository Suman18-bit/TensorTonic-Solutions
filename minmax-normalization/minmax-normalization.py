import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    X = np.asarray(X, dtype=float)
    
    X_min = np.min(X, axis=axis, keepdims=True)
    X_max = np.max(X, axis=axis, keepdims=True)
    
    X_scaled = (X - X_min) / (X_max - X_min + eps)
    
    return X_scaled