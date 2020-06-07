def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # Create a dict with the index positions and weight values
    # Look for pairs by looping through the weights, checking our dictionary for a number that is equal to the limit minus the current weight(target weight)
    
    cache = {}

    for i in range(length):
        cache[weights[i]] = i
    
    for i, w in enumerate(weights):
        targetWeight = limit - w
        if targetWeight in cache:
            if i > cache[targetWeight]:
                return (i, cache[targetWeight])
            return (cache[targetWeight], i)
           
    return None
    