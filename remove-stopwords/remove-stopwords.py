def remove_stopwords(text, custom_stopwords=None):
    """
    Remove common English stop words (Case-Sensitive).
    """
    default_stopwords = {
        'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 
        'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'before', 
        'being', 'below', 'between', 'both', 'but', 'by', 'can', 'did', 'do', 
        'does', 'doing', 'down', 'during', 'each', 'few', 'for', 'from', 'further', 
        'had', 'has', 'have', 'having', 'he', 'her', 'here', 'hers', 'herself', 
        'him', 'himself', 'his', 'how', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 
        'itself', 'just', 'me', 'more', 'most', 'my', 'myself', 'no', 'nor', 'not', 
        'of', 'off', 'on', 'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves', 
        'out', 'over', 'own', 'same', 'she', 'should', 'so', 'some', 'such', 'than', 
        'that', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 
        'these', 'they', 'this', 'those', 'through', 'to', 'too', 'under', 'until', 
        'up', 'very', 'was', 'we', 'were', 'what', 'when', 'where', 'which', 'while', 
        'who', 'whom', 'why', 'will', 'with', 'you', 'your', 'yours', 'yourself', 'yourselves'
    }
    
    stop_words = set(custom_stopwords) if custom_stopwords is not None else default_stopwords
    
    is_string = isinstance(text, str)
    tokens = text.split() if is_string else text
    
    # FIX: Removed .lower() so "The" and "THE" do not match lowercase "the"
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    return " ".join(filtered_tokens) if is_string else filtered_tokens