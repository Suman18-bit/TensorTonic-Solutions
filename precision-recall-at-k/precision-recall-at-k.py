def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    
    Args:
        recommended (list): List of items recommended to the user.
        relevant (list or set): Ground truth list/set of relevant items.
        k (int): The cutoff threshold.
        
    Returns:
        list: [precision_at_k, recall_at_k]
    """
    k = int(k)
    if k <= 0:
        return [0.0, 0.0]
        
    recommended_at_k = recommended[:k]
    if not recommended_at_k:
        return [0.0, 0.0]
        
    relevant_set = set(relevant)
    hits = sum(1 for item in recommended_at_k if item in relevant_set)
    
    precision = hits / k
    
    if len(relevant_set) == 0:
        recall = 0.0
    else:
        recall = hits / len(relevant_set)
        
    # Returning a list instead of a tuple
    return [precision, recall]