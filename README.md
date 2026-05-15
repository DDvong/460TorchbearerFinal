# The Torchbearer

**Student Name:** Dylan Vongkaysone
**Student ID:** 828232529
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
- We have to visit every relic chamber once but the path shows how to go to the cheapest nodes to the end but without considering the potential total minimum cost that comes from visiting all nodes.
  _Your answer here._

- **What decision remains after all inter-location costs are known:**
- After finding the cost from u to v, we have to find the optimal fuel consumption order as there are different orders that results in minimum cost.
  _Your answer here._

- **Why this requires a search over orders (one sentence):**
- We search over orders to identify different orders to find the minimum fuel cost.
  _Your answer here._

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source |
|---|---|
| Entrance Node (S) | Starting point |
| Relic Chambers(M) | Subsequent goal nodes to travel from a node to another node |

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer |
|---|---|
| Data structure name | Dictionary |
| What the keys represent | Individual Destination Nodes |
| What the values represent | Minimum Fuel Cost |
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | Hash Table |

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** k + 1
- **Cost per run:** O(m log n)
- **Total complexity:** O(k * m log n)
- **Justification (one line):** Running Dijkstra from source to every k relic chambers node to find the shortest path

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  A node being finalized means their distance is the shortest path possible.

- **For nodes not yet finalized (not in S):**
  A node not yet finalized means its the shortest path thats been discovered thus far.

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  Source node is initialized to zero, all other nodes are set to infinity. No path has been discovered, the only shortest path is S.
  
- **Maintenance : why finalizing the min-dist node is always correct:**
  As edge weights are non-negative, dist[u] is the shortest discovered path using finalized min-dist nodes.
  
- **Termination : what the invariant guarantees when the algorithm ends:**
  Finalized nodes are the shortest and cheapest path calculated in the graph.

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

The Torchbearer's planner correct routing decisions applies correct distances to get the efficient path

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** Greedy looks for lowest number and it does not account for potential future paths that are cheaper overall.
- **Counter-example setup:** With entrance Node S. relics B, C, D, and exit node T, but B -> D = 3
- **What greedy picks:** Route: S -> B -> D -> C -> T total fuel = 1 + 3 + 1 + 1 = 6
- **What optimal picks:** Route: S -> D -> C -> B -> T total fuel = 2 + 1 + 1 + 1 = 5 
- **Why greedy loses:** Greedy loses because it only focuses on the cheapest cost, when it doesn't consider all routes that are possibly cheaper overall. 

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- Greedy doesn't focus on the order of all possible routes to potentially get a cheaper route, by not doing so it only commits to the cheapest cost.

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
