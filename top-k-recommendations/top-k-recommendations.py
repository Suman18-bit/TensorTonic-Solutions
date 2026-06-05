def top_k_recommendations(scores, rated_indices, k):
    """
    Return indices of top-k unrated items by predicted score.
    """
    k = int(k)
    if k <= 0:
        return []
        
    # Convert to set for fast O(1) lookups
    rated_set = set(rated_indices)
    
    # Pair indices with scores, keeping only the unrated items
    unrated_scored_items = [
        (idx, score) for idx, score in enumerate(scores) if idx not in rated_set
    ]
    
    # Sort unrated items by score in descending order
    unrated_scored_items.sort(key=lambda x: x[1], reverse=True)
    
    # Extract just the item indices for the top-k items
    top_k_indices = [idx for idx, score in unrated_scored_items[:k]]
    
    return top_k_indices