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
