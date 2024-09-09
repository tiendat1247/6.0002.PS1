###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    #define a empty dictionary 
    cow_dict = {}
    #open file, loop through each line
    with open(filename,'r') as file:
        for file_line in file:
    #split name and weight to dict
            name, weight = file_line.strip().split(',')
            cow_dict[name] = int(weight)
    #return dictionary
    return cow_dict

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    # Define variable to store trip
    trips =[]
    # Make a shallow copy of cows, sort by weight, descending
    cows_copy = sorted(cows.items(), key = lambda item: item[1], reverse= True)
    # Condition to stop transporting
    while cows_copy:
        current_trip = []  # List to store the current trip
        current_weight = 0  # Track the total weight of the current trip

        # Make a copy of cows_copy to iterate over since we'll be modifying cows_copy during the loop
        cows_left = cows_copy[:]

        # Try to fill the current trip with the heaviest cows that fit
        for cow in cows_left:
            cow_name, cow_weight = cow
            cow_weight = int(cow_weight)

            # If adding this cow doesn't exceed the weight limit, add it to the trip
            if current_weight + cow_weight <= limit:
                current_trip.append(cow_name)
                current_weight += cow_weight
                # Remove the cow from cows_copy since it's been assigned to a trip
                cows_copy.remove(cow)

        # Add the current trip to the list of all trips
        trips.append(current_trip)

    # Return the list of trips
    return trips

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    # Initialize variable to store best partion of trips
    best_trip_partition = None
    cows_copy = cows.copy()
    # Use the cow names as a set
    cow_names = set(cows.keys())
    # Enumarate all partition of cows
    for partition in get_partitions(cow_names):
        valid_partition = True
        # Check each trip in the partition
        for trip in partition:
            trip_weight = sum(int(cows[cow]) for cow in trip)
            # Handle if the trip exceed the weight limit
            if trip_weight > limit:
                valid_partition = False
                break
            # If the partition is valid and is the best
            if valid_partition and (best_trip_partition is None or len(partition) < len(best_trip_partition)):
                best_trip_partition = partition
    return [list(trip) for trip in best_trip_partition]
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    # Store the parameter
    filename = "C:\\Users\\PC\\Downloads\\687c3ee2bee6229f46968d366a92345e_PS1\\ps1_cow_data.txt"
    cows = load_cows(filename)
    limit = 10
    # Measure the execution of greedy algorithm
    start_time = time.time()
    # Call GDA
    greed_transport = greedy_cow_transport(cows, limit)
    # End time
    end_time = time.time()
    elapsed_time = end_time - start_time
    # Measure the execution of Brute Force Alogorithm
    start_time_b = time.time()
    # Call BFA
    brute_force_transport = brute_force_cow_transport(cows, limit)
    # End time
    end_time_b = time.time()
    elapsed_time_b = end_time_b - start_time_b

    print(f"Greedy algorithm: {greed_transport} and takes {elapsed_time:.4f} seconds")
    print(f"Brute Force algorithm: {brute_force_transport} and takes {elapsed_time_b:.4f} seconds")

def main():
    compare_cow_transport_algorithms()

if __name__ =="__main__":
    main()
