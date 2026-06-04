import numpy as np
from sklearn.metrics.pairwise import cosine_similarity as skl_cosine_similarity

def cosine_similarity(a, b):
    a = np.array(a).reshape(1, -1)
    b = np.array(b).reshape(1, -1)
    
    return float(skl_cosine_similarity(a, b)[0, 0])
