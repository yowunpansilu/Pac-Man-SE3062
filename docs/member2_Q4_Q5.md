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

---

## Q5: Finding All the Corners

### The problem

Pacman must touch all four corners of the maze. Position alone is not enough as a state: being
at square (5, 3) with no corners visited is a very different situation from being there with
three corners visited. So the state has to remember which corners are done.

### State representation

```python
state = (position, visitedCorners)
# position       = (x, y)
# visitedCorners = (bool, bool, bool, bool), in the same order as self.corners
```

Why this design:

- **Small:** a position plus four flags. It does not store the wall grid or the whole
  `GameState`, which the assignment says not to do.
- **Hashable:** it is made only of tuples, so it works in the expanded set and as a dictionary key.
- **Finite:** at most (number of open squares × 2⁴) states. mediumCorners has 3,032 reachable
  states.

### The three methods

| Method | What it does |
|---|---|
| `getStartState` | Returns `(startingPosition, flags)`. A corner is already marked visited if Pacman starts on it. |
| `isGoalState` | `all(visitedCorners)`: true only when all four corners are visited. |
| `getSuccessors` | For North, South, East and West, finds the next square with `Actions.directionToVector`. Skips walls. Copies the flags and marks a corner visited if the next square is that corner. Every step costs 1. |

The flags are tuples, so a new tuple is built for each successor instead of changing the parent's
flags. The `self._expanded += 1` line was left exactly as given, because the autograder counts
nodes with it.

### Results

| Test | Result |
|---|---|
| `python autograder.py -q q5` | 3/3 (runs Q2 first as a dependency) |
| tinyCorner | 28-step solution |
| mediumCorners with BFS | optimal path of 106, 1,966 nodes |
| mediumCorners with A* + cornersHeuristic (Q6) | optimal path of 106, 189 nodes |

### How Q5 connects to Q6

Member 3's `cornersHeuristic` unpacks the state as `position, visitedCorners = state`, so it
depends on exactly this format. If the Q5 state ever changed, Q6 would have to change with it.

### Commits

- `8c3edb3` Q5: define CornersProblem state (position, visited-corner flags) in getStartState
- `c55af1b` Q5: implement isGoalState for corners
- `ba8b79f` Q5: implement getSuccessors with visited-corner bookkeeping
