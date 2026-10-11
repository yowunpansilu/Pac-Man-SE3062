# Group Work Division (IT3012 Pac-Man Search)

| Member | Code tasks | Marks owned | Extra duties |
|---|---|---|---|
| M1 | Q1 DFS, Q2 BFS, Q3 UCS (`search.py`) | 12 | Create public Git repo and branch rules; merge `search.py`; final ZIP and submission |
| M2 | Q4 A*, Q5 CornersProblem (`search.py`, `searchAgents.py`) | 12 | Integration testing: run the full autograder on the merged code |
| M3 | Q6 cornersHeuristic (`searchAgents.py`) | 8 | Write the admissibility/consistency proofs; collect Git screenshots and the contribution table |
| M4 | Q7 foodHeuristic (`searchAgents.py`) | 8 | Assemble Report.pdf (Q1-Q7 sections, AI declaration, repo link) |

## Reasoning
- **Marks are balanced.** Q1-Q4 are 4 marks each, and Q5, Q6 and Q7 are 8 each (40 total).
  M1 and M2 get 12 marks of easier work. M3 and M4 get 8 marks each of the hardest work,
  because the heuristics are scored on nodes expanded and a non-admissible heuristic scores 0.
- **Dependencies are handled.** Q1-Q3 share the same graph-search skeleton and only change the
  fringe, so one person writes all three consistently. A* (Q4) is the same skeleton again, so M2
  takes it, and Q5 is where M2 gets practice with state representation. Q6 needs Q5's
  `CornersProblem`, so M3 starts once M2 has pushed it (use a stub state meanwhile).
  Q7 depends only on the provided `FoodSearchProblem`, so M4 can start on day one.
- **Merge conflicts are minimized.** M1 owns `search.py`, and M2-M4 each work in separate
  functions in `searchAgents.py`. Each person works on their own branch and opens PRs.
- **Evaluation criteria.**
  - Git (10 marks, individual): everyone needs frequent, descriptive commits over the whole
    timeline, so no one commits only at the end. Commit in small steps, such as "implement
    BFS fringe" and "fix heuristic for goal state".
  - Viva (40 marks, individual): you are marked on the *whole* solution, not just your part.
    Each person must explain DFS/BFS/UCS/A*, fringe mechanics and optimality, and defend
    all heuristics.
  - Report (10 marks, group): per-question code, autograder screenshot, and an explanation
    of at most 200 words. It also needs the repo link, Git evidence, contribution table and
    AI declaration.

## Cross-review (protects the viva marks)
- M1 reviews M2's code.
- M2 reviews M3's code.
- M3 reviews M4's code.
- M4 reviews M1's code.
- Before the viva, each member explains every question to the others, with extra practice on the
  admissibility proofs for Q6 and Q7.

## Suggested timeline
1. Day 1: M1 creates the repo. Everyone clones the repo and sets up the conda environment.
2. Days 2-4: implementation on branches, with PRs reviewed by the assigned reviewer.
3. Day 5: merge, run `python autograder.py` on everything, and fix any failures.
4. Day 6: write the report, take the screenshots, and do viva practice.
5. Day 7: submit `Group_X_Report.pdf` and `Group_X_Code.zip`, containing only `search.py` and `searchAgents.py`.

## Submission checklist
- [ ] Do not rename files, functions or classes.
- [ ] Q6 heuristic is admissible and consistent: it returns 0 at a goal and is never negative.
- [ ] Q7 heuristic is admissible and consistent.
- [ ] Autograder screenshots for Q1-Q7.
- [ ] Public repo link, commit history screenshots and contribution graphs.
- [ ] Contribution table (names, IDs, tasks).
- [ ] AI usage declaration with the exact prompts, or "No AI tools were utilized."
