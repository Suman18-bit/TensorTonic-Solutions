import numpy as np

def rnn_step_forward(x_t, h_prev, Wx, Wh, b):
    """
    Computes a single RNN forward step.
    Returns: h_t of shape (H,) or (N, H)
    """
    x_t = np.asarray(x_t)
    h_prev = np.asarray(h_prev)
    
    # Calculate the next hidden state
    h_t = np.tanh(np.dot(x_t, Wx) + np.dot(h_prev, Wh) + b)
    
    # FIX: Access .shape without parentheses
    # If h_t is (N, H), then H is the second element
    shape_tuple = h_t.shape 
    
    # Return the hidden state array (this is what the next step needs)
    return h_t

