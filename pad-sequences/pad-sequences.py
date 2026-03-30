import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # 1. Handle empty input case
    if not seqs:
        return np.empty((0, max_len or 0))

    # 2. Determine target length (L)
    actual_max = max(len(seq) for seq in seqs)
    L = max_len if max_len is not None else actual_max
    N = len(seqs)

    # 3. Pre-allocate the result array with the pad_value
    # Use the data type of the first element to keep it consistent
    dtype = np.array(seqs[0]).dtype if len(seqs[0]) > 0 else float
    result = np.full((N, L), pad_value, dtype=dtype)

    # 4. Fill the array with sequences
    for i, seq in enumerate(seqs):
        # Truncate if sequence is longer than max_len
        trunc_seq = seq[:L]
        # Place the sequence at the beginning of the row (pre-padding)
        result[i, :len(trunc_seq)] = trunc_seq

    return result
    pass