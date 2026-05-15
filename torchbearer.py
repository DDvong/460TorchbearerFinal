"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: ___________________________
Student ID:   ___________________________

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    TODO
    """
    return """
    - Why a single shortest-path run from S is not enough:
    We have to visit every relic chamber once but the path shows how to go to the cheapest nodes to the end but without considering the potential total minimum cost that comes from visiting all nodes.

    - What decision remains after all inter-location costs are known:
    After finding the cost from u to v, we have to find the optimal fuel consumption order as there are different orders that results in minimum cost.

    - Why this requires a search over orders (one sentence):
    We search over orders to identify different orders to find the minimum fuel cost. """

    

# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    TODO 
    """
    #create a list for starting entrance and add relic chambers
    source_node = [spawn] + relics
    return source_node
    pass


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    TODO
    """
    #create empty dictionary to record minimum fuel consumption
    distance = {}
    #intialize all nodes to infinity, source starting node to 0
    for node in graph:
        distance[node] = float('inf')
    distance[source] = 0

    #intializing heap with starting node that is storing pairs of (cost,node)
    heap = []
    heapq.heappush(heap, (0, source)) #add the entrance node with cost 0, node 'S'
    
    while heap:
        curr_cost, node = heapq.heappop(heap) #pop the node with the smallest current distance cost
        #skipping paths that are longer than current best paths
        if curr_cost > distance[node]:
            continue

        #explores the edges of the current node
        for neighbor, weight in graph[node]: 
              new_cost = curr_cost + weight #total distance it takes to reach the neighbor node from the current node

              if new_cost < distance[neighbor]: #if the new path is cheaper than the current minimum cost 
                distance[neighbor] = new_cost #update the update the dictionary of minimum cost
                heapq.heappush(heap, (new_cost, neighbor)) #push neigbor nodes into heap to be explored after curr_node
            
    return distance #returns the shortest distance from the source to the nodes

    pass


def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    TODO
    """
    #create empty dictionary to store shortest distances
    distance_table = {}
    #helper functions 
    #retrieves source nodes and run dijkstra for each node
    for source in select_sources(spawn, relics, exit_node): 
        distance_table[source] = run_dijkstra(graph, source) #storing shortest distance

    return distance_table

    pass


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    return """
    Part 3a:
    - For nodes already finalized (in S): A node being finalized means their distance is the shortest path possible.
    - For nodes not yet finalized (not in S): A node not yet finalized means its the shortest path thats been discovered thus far.

    Part 3b:
    - Source node is initialized to zero, all other nodes are set to infinity. No path has been discovered, the only shortest path is S.
    - As edge weights are non-negative, dist[u] is the shortest discovered path using finalized min-dist nodes.
    - Finalized nodes are the shortest and cheapest path calculated in the graph.

    Part 3c:
    -The Torchbearer's planner correct routing decisions applies correct distances to get the efficient path.
    """



# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    return """
    Part 4:
    - The failure mode: Greedy looks for lowest number and it does not account for potential future paths that are cheaper overall.
    - Counter-example setup: With entrance Node S. relics B, C, D, and exit node T, but B -> D = 3
    - What greedy picks: Route: S -> B -> D -> C -> T total fuel = 1 + 3 + 1 + 1 = 6
    - What optimal picks: Route: S -> D -> C -> B -> T total fuel = 2 + 1 + 1 + 1 = 5
    - Why greedy loses: Greedy loses because it only focuses on the cheapest cost, when it doesn't consider all routes that are possibly cheaper overall.
    - What the Algorithm Must Explore: Greedy doesn't focus on the order of all possible routes to potentially get a cheaper route, by not doing so it only commits to the cheapest cost.
    """


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    #intialization
    current_loc = spawn
    relics_remaining = list(relics)
    relics_visited_order = []
    cost_so_far = 0.0
    best = [float('inf'), []] #holds the best minimum cost and ordered relic list

    #calls the search
    _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best)

    return tuple(best)
    pass


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    pass


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
