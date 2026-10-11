# Member 2: Q4 A* Search and Q5 Corners Problem

**Member:** Thinila N.A.D.I.D. (IT24102032), GitHub [@isurudevthilina](https://github.com/isurudevthilina)
**Files:** `search.py` (Q4), `searchAgents.py` (Q5)
**Branches:** `Q4_aStarSearch` (PR #2), `Q5_cornersProblem` (PR #3)

---

## Q4: A* Search

### What A* does

A* picks the fringe node with the smallest

> f(n) = g(n) + h(n)

where **g(n)** is the cost already paid to reach *n* and **h(n)** is the heuristic's estimate of
the cost still to go. UCS only looks at g, so it spreads out evenly in every direction. A* also
looks at h, so it leans towards the goal.

### How the code works

`aStarSearch(problem, heuristic)` uses the same graph-search loop as UCS:

1. Push `(start, [], 0)` onto a `util.PriorityQueue` with priority `h(start)`.
2. Pop the node with the smallest f.
3. If it is a goal, return its path. The goal test is done **when the node is popped**, not when
   it is pushed, because a cheaper path to the goal may still be on the fringe
   (`astar_3_goalAtDequeue` tests this).
4. If the state is not yet in `bestCost`, record it and push every successor that is not yet
   expanded, with `g' = g + stepCost` and priority `g' + h(successor)`.
5. If the fringe empties, return `[]`.

The `bestCost` dictionary is the expanded set: once a state is popped, it is never expanded again.

### Why it is optimal

- With an **admissible** heuristic (h never overestimates), A* finds an optimal path.
- With a **consistent** heuristic (h(s) ≤ cost(s, s′) + h(s′)), f never decreases along a path,
  so the first time a state is popped it already has its cheapest cost. That is what makes the
  graph-search version (never expanding a state twice) safe.
- With `nullHeuristic` (h = 0), f = g and A* behaves exactly like UCS.

### Results

| Test | Result |
|---|---|
| `python autograder.py -q q4` | 3/3, all 6 tests pass |
| mediumMaze, Manhattan heuristic | optimal path of 68, 221 nodes (UCS: 269) |
| bigMaze, Manhattan heuristic | optimal path of 210, 549 nodes (UCS: 620) |

### Commit

`28de7d8` Q4: implement A* search with f = g + h on util.PriorityQueue
