# The Torchbearer

**Student Name:** Dylan Vongkaysone
**Student ID:** 828232529
**Course:** CS 460 – Algorithms | Spring 2026

---

## Part 1: Problem Analysis

- **Why a single shortest-path run from S is not enough:**
- We have to visit every relic chamber once but the path shows how to go to the cheapest nodes to the end but without considering the potential total minimum cost that comes from visiting all nodes.

- **What decision remains after all inter-location costs are known:**
- After finding the cost from u to v, we have to find the optimal fuel consumption order as there are different orders that results in minimum cost.

- **Why this requires a search over orders (one sentence):**
- We search over orders to identify different orders to find the minimum fuel cost.
---

## Part 2: Precomputation Design

### Part 2a: Source Selection

| Source Node Type | Why it is a source |
|---|---|
| Entrance Node (S) | Starting point |
| Relic Chambers(M) | Subsequent goal nodes to travel from a node to another node |

### Part 2b: Distance Storage

| Property | Your answer |
|---|---|
| Data structure name | Dictionary |
| What the keys represent | Individual Destination Nodes |
| What the values represent | Minimum Fuel Cost |
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | Hash Table |

### Part 2c: Precomputation Complexity

- **Number of Dijkstra runs:** k + 1
- **Cost per run:** O(m log n)
- **Total complexity:** O(k * m log n)
- **Justification (one line):** Running Dijkstra from source to every k relic chambers node to find the shortest path

---

## Part 3: Algorithm Correctness

### Part 3a: What the Invariant Means

- **For nodes already finalized (in S):**
  A node being finalized means their distance is the shortest path possible.

- **For nodes not yet finalized (not in S):**
  A node not yet finalized means its the shortest path thats been discovered thus far.

### Part 3b: Why Each Phase Holds

- **Initialization : why the invariant holds before iteration 1:**
  Source node is initialized to zero, all other nodes are set to infinity. No path has been discovered, the only shortest path is S.
  
- **Maintenance : why finalizing the min-dist node is always correct:**
  As edge weights are non-negative, dist[u] is the shortest discovered path using finalized min-dist nodes.
  
- **Termination : what the invariant guarantees when the algorithm ends:**
  Finalized nodes are the shortest and cheapest path calculated in the graph.

### Part 3c: Why This Matters for the Route Planner

The Torchbearer's planner correct routing decisions applies correct distances to get the efficient path

---

## Part 4: Search Design

### Why Greedy Fails

- **The failure mode:** Greedy looks for lowest number and it does not account for potential future paths that are cheaper overall.
- **Counter-example setup:** With entrance Node S. relics B, C, D, and exit node T, but B -> D = 3
- **What greedy picks:** Route: S -> B -> D -> C -> T total fuel = 1 + 3 + 1 + 1 = 6
- **What optimal picks:** Route: S -> D -> C -> B -> T total fuel = 2 + 1 + 1 + 1 = 5 
- **Why greedy loses:** Greedy loses because it only focuses on the cheapest cost, when it doesn't consider all routes that are possibly cheaper overall. 

### What the Algorithm Must Explore

- Greedy doesn't focus on the order of all possible routes to potentially get a cheaper route, by not doing so it only commits to the cheapest cost.

---

## Part 5: State and Search Space

### Part 5a: State Representation

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | current_loc | node | Starting location of spawn |
| Relics already collected | relics_remaining | list | Relics that are not visited yet |
| Fuel cost so far | cost_so_far | float | Collected fuel cost |

### Part 5b: Data Structure for Visited Relics

| Property | Your answer |
|---|---|
| Data structure chosen | list |
| Operation: check if relic already collected | Time complexity: O(n)|
| Operation: mark a relic as collected | Time complexity: O(n) |
| Operation: unmark a relic (backtrack) | Time complexity: O(1) |
| Why this structure fits | Ordered list |

### Part 5c: Worst-Case Search Space

- **Worst-case number of orders considered:** k!
- **Why:** Visiting every possible route

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

- **What is tracked:** The best possible minimum fuel cost (minimum_fuel_cost) and the ordered route it achieved with it (ordered_relic_list).
- **When it is used:** Used when current route's cost exceeds the best complete route found so far.
- **What it allows the algorithm to skip:** Skip when current cost in the route exceeds the best cost of another route.

### Part 6b: Lower Bound Estimation

- **What information is available at the current state:** Current location, relics remaining, fuel cost so far, a best route.
- **What the lower bound accounts for:** Remaining overall cheapest cost. 
- **Why it never overestimates:** The remaining relic costs are at the minimum cost computed from dijkstra

### Part 6c: Pruning Correctness

-Due to non-negative costs, a branch that exceed the current best minimum path skips as'll increase the total cost from the current best.

---

## References

-Youtube videos for visualization, such as Abdul Bari, ByteQuest.
