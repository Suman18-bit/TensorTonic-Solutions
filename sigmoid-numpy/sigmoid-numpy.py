import numpy as np
def sigmoid(x):
    x = np.asarray(x)
    s=1/(1+np.exp(-x))
    return s