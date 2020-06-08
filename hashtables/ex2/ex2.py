#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    for t in tickets:
        cache[t.source] = t.destination
    
    route = [cache["NONE"]]

    for t in tickets:

        nextT = route[-1]
        route.append(cache[nextT])

        if route[-1] == "NONE":
            return route

