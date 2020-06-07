def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    for n in a:
        cache[n] = n
    
    for n in a:
        targetNum = 0
        if n > 0:
            targetNum = n * -1
            if targetNum in cache:
                result.append(n)
    
    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
