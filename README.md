# Search Algorithms in Pac-Man (SE3062 Group Assignment)

SE3062 Intelligent Systems, Year 3, 2026, Faculty of Computing, SLIIT. Group **2026-AI-33**.

This repository contains our solution to the UC Berkeley CS188 Pac-Man search project. We
implemented four classic search algorithms (DFS, BFS, UCS and A*), a new search problem that
visits all four corners of a maze, and two admissible, consistent heuristics.

## Results

All questions pass the autograder on the `main` branch.

| Question | Function(s) | File | Autograder |
|---|---|---|---|
| Q1 Depth First Search | `depthFirstSearch` | `search.py` | 3/3 |
| Q2 Breadth First Search | `breadthFirstSearch` | `search.py` | 3/3 |
| Q3 Uniform Cost Search | `uniformCostSearch` | `search.py` | 3/3 |
| Q4 A* Search | `aStarSearch` | `search.py` | 3/3 |
| Q5 Finding All the Corners | `CornersProblem` | `searchAgents.py` | 3/3 |
| Q6 Corners Heuristic | `cornersHeuristic` | `searchAgents.py` | 3/3 (189 nodes) |
| Q7 Food Heuristic | `foodHeuristic` | `searchAgents.py` | 5/4 (255 nodes) |

## Requirements

- Python 3.9 to 3.11 (the course recommends 3.11)
- `numpy` and `matplotlib` (only needed by the course environment, not by our code)

```bash
conda create -n cs188 python=3.11
conda activate cs188
pip install numpy matplotlib
```

Check the setup by playing a game with the arrow keys:

```bash
python pacman.py
```

## Project structure

| File | Role | Description |
|---|---|---|
| `search.py` | **Edited** | DFS, BFS, UCS and A* (Q1 to Q4) |
| `searchAgents.py` | **Edited** | `CornersProblem`, `cornersHeuristic` and `foodHeuristic` (Q5 to Q7) |
| `util.py` | Read only | `Stack`, `Queue` and `PriorityQueue`, which every algorithm must use |
| `pacman.py` | Reference | Runs the game and defines `GameState` |
| `game.py` | Reference | `Agent`, `Directions`, `Actions` and `Grid` |
| `autograder.py` | Run | Grades each question using the files in `test_cases/` |
| `layouts/` | Data | Maze layouts used by the commands below |
| `contribution.md` | Plan | Our work division, review pairs and timeline |

## Running the autograder

```bash
python autograder.py                    # all questions
python autograder.py -q q4              # one question
python autograder.py -q q6 --no-graphics
```

`python run_tests.py` (added on the integration-testing branch) runs Q1 to Q7 one by one and
prints a summary table.

## Watching each algorithm

These commands open the game window. Add `-q` to skip the graphics, or `-z 0.5` to zoom out on
big mazes. The numbers come from our final code.

| Question | Command | Path cost | Nodes expanded |
|---|---|---|---|
| Q1 DFS | `python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs` | 130 | 146 |
| Q2 BFS | `python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs` | 68 | 269 |
| Q3 UCS | `python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs` | 68 | 269 |
| Q3 StayEast | `python pacman.py -l mediumDottedMaze -p StayEastSearchAgent` | 1 | 186 |
| Q3 StayWest | `python pacman.py -l mediumScaryMaze -p StayWestSearchAgent` | 68719479864 | 108 |
| Q4 A* vs UCS | `python pacman.py -l bigMaze -z 0.5 -p SearchAgent -a fn=ucs` | 210 | 620 |
| Q4 A* | `python pacman.py -l bigMaze -z 0.5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic` | 210 | 549 |
| Q5 Corners (BFS) | `python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem` | 106 | 1966 |
| Q6 Corners (A*) | `python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5` | 106 | 189 |
| Q7 Food (A*) | `python pacman.py -l trickySearch -p AStarFoodSearchAgent` | 60 | 255 |

The huge cost for `StayWestSearchAgent` is expected: its cost function makes every step on the
east side extremely expensive, so UCS stays on the west side.

Comparing the rows shows why heuristics matter. With the same optimal path, A* expands 549 nodes
on `bigMaze` against 620 for UCS, and `cornersHeuristic` cuts the corners search from 1966 nodes
(BFS) to 189.

## Team

| Member | Student ID | GitHub | Questions |
|---|---|---|---|
| Withanan W.Y.P. | IT24102008 | [@yowunpansilu](https://github.com/yowunpansilu) | Q1, Q2, Q3; repository setup and merges |
| Thinila N.A.D.I.D. | IT24102032 | [@isurudevthilina](https://github.com/isurudevthilina) | Q4, Q5; integration testing |
| Maduwatta U.S.T. | IT24102088 | [@SupunThk](https://github.com/SupunThk) | Q6; heuristic proofs |
| Karunarathna H.R.A. | IT24102885 | [@rusiru-242](https://github.com/rusiru-242) | Q7; report |

See `contribution.md` for the full work division and review pairs.

## Workflow

Q4, Q5 and Q7 were built on their own branches (`Q4_aStarSearch`, `Q5_cornersProblem` and
`Q7_foodHeuristic`) and merged into `main` with pull requests. The other questions were
committed directly to `main`. Do not rename files, functions or classes: the autograder imports
them by name.
