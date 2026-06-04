import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Returns positional encoding (PE) of shape (seq_len, d_model)
    using sine and cosine formulations.
    If d_model is odd, the last column is sine.
    """
    # Positions: 0, 1, ..., seq_len-1
    positions = np.arange(seq_len)[:, np.newaxis]
    
    # Dimensions: 0, 1, ..., d_model-1
    dims = np.arange(d_model)[np.newaxis, :]
    
    # Compute angle rates
    angle_rates = 1 / np.power(base, (dims // 2) * 2 / d_model)
    angle_rads = positions * angle_rates
    
    # Apply sine to even indices, cosine to odd indices
    pe = np.zeros((seq_len, d_model))
    pe[:, 0::2] = np.sin(angle_rads[:, 0::2])
    pe[:, 1::2] = np.cos(angle_rads[:, 1::2])
    
    # If d_model is odd, last column is sine
    if d_model % 2 == 1:
        pe[:, -1] = np.sin(angle_rads[:, -1])
    
    return pe
