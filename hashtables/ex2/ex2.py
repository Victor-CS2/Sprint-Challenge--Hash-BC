#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source # starting airport
        self.destination = destination # next airport

# first flight ticket should have a source of "none" and the final ticket should have a destination of "none"
def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for ticket in tickets:
        source = ticket.source
        destination = ticket.destination
        hash_table_insert(hashtable, source, destination)
    
    take_off = hash_table_retrieve(hashtable, "NONE") # The first ticket must have NONE as the source
    # set the first ticket as the beginning of the route.
    route[0] = take_off # so the "zeroth" index of route should be equal to first ticket

    # iterate through the hashtable
    for i in range(1, length):
        final_approach = hash_table_retrieve(hashtable, take_off) # gets the source of the last ticket and set it to the next route
        route[i] = final_approach
        take_off = final_approach

    # function should output an array of strings with the entire route of your trip
    return route