# Integration Testing (Member 2)

After all four members' code was merged into `main`, I tested the combined `search.py` and
`searchAgents.py` together. That matters here because the questions depend on each other: Q5
reuses BFS from Q2, Q6 needs the Q5 state format and the Q4 A* search, and Q7 also runs on A*.

**Tested commit:** `fa410e1` on `main` (11 October 2026)
**Environment:** Python 3.11.9 on macOS 26.5

## 1. Full autograder run

```bash
python autograder.py --no-graphics
```

| Question | Score | Notes |
|---|---|---|
| Q1 Depth First Search | 3/3 | |
| Q2 Breadth First Search | 3/3 | |
| Q3 Uniform Cost Search | 3/3 | |
| Q4 A* Search | 3/3 | |
| Q5 Corners Problem | 3/3 | Runs Q2 first (dependency) |
| Q6 Corners Heuristic | 3/3 | 189 nodes on mediumCorners (full marks needs at most 1200) |
| Q7 Food Heuristic | 5/4 | 255 nodes on trickySearch, includes extra credit (at most 7000) |

Q8 (closest-dot search) is not part of this assignment, but it also passes (3/3).

## 2. Results for each test case

Every test case passed. The node counts are what the autograder printed.

| Question | Test case | What it checks | Result |
|---|---|---|---|
| Q1 | graph_backtrack, graph_bfs_vs_dfs, graph_infinite, graph_manypaths | Small graphs: correct path and expansion order, no infinite loop on cycles | PASS |
| Q1 | pacman_1 | mediumMaze: path length 130, 146 nodes expanded | PASS |
| Q2 | graph_backtrack, graph_bfs_vs_dfs, graph_infinite, graph_manypaths | Same graphs, BFS expansion order | PASS |
| Q2 | pacman_1 | mediumMaze: optimal path length 68, 269 nodes expanded | PASS |
| Q3 | graph_* (4 tests), ucs_0_graph | Small graphs with step costs | PASS |
| Q3 | ucs_1_problemC | mediumMaze, normal costs: length 68, 269 nodes | PASS |
| Q3 | ucs_2_problemE | mediumMaze, StayEast costs: length 74, 260 nodes | PASS |
| Q3 | ucs_3_problemW | mediumMaze, StayWest costs: length 152, 173 nodes | PASS |
| Q3 | ucs_4_testSearch | testSearch: length 7, 14 nodes | PASS |
| Q3 | ucs_5_goalAtDequeue | Goal test must happen when the node is popped | PASS |
| Q4 | astar_0, astar_1_graph_heuristic | Small graphs with a heuristic | PASS |
| Q4 | astar_2_manhattan | mediumMaze with Manhattan heuristic: length 68, 221 nodes | PASS |
| Q4 | astar_3_goalAtDequeue, graph_backtrack, graph_manypaths | Goal at dequeue, backtracking | PASS |
| Q5 | corner_tiny_corner | tinyCorner: 28-step solution | PASS |
| Q6 | 3 admissibility checks | h(start) is at most the true cost on three layouts | PASS |
| Q6 | expansion test | mediumCorners: 189 nodes, path length 106 | PASS |
| Q7 | food_heuristic_1 to food_heuristic_17 | h is admissible and consistent on 17 small food layouts | PASS |
| Q7 | food_heuristic_grade_tricky | trickySearch: 255 nodes | PASS |

## 3. Running the tests yourself

`run_tests.py` (on the `test/integration-runner` branch) runs each question in its own process
and prints one summary row per question, with a non-zero exit code if anything fails:

```bash
python run_tests.py          # Q1 to Q7
python run_tests.py q4 q5    # only some questions
python run_tests.py -v       # show the full output of failed questions
```
