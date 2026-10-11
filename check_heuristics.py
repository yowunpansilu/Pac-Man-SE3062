"""Exhaustive admissibility and consistency check for the Q6 and Q7 heuristics.

The autograder only samples a few states. This script visits EVERY reachable
state of some small layouts and checks, for each state s and successor s':

    h(s) >= 0                       (never negative)
    h(goal) == 0                    (zero at every goal)
    h(s) <= cost(s, s') + h(s')     (consistent)

Consistency together with h(goal) == 0 implies admissibility. As an extra
check, h(start) is compared with the optimal solution cost found by UCS.

Usage:
    python check_heuristics.py
"""

import layout
import pacman
import search
import searchAgents
import util


def loadState(layoutName):
    """Build the starting GameState for a layout, with no ghosts."""
    state = pacman.GameState()
    state.initialize(layout.getLayout(layoutName), 0)
    return state


def reachableStates(problem):
    """Breadth-first enumeration of every state reachable from the start."""
    start = problem.getStartState()
    seen = {start}
    queue = util.Queue()
    queue.push(start)
    while not queue.isEmpty():
        state = queue.pop()
        yield state
        for successor, _action, _cost in problem.getSuccessors(state):
            if successor not in seen:
                seen.add(successor)
                queue.push(successor)


def check(problemClass, heuristic, layoutName):
    """Return (states checked, list of violations, h(start), optimal cost)."""
    problem = problemClass(loadState(layoutName))
    violations = []
    count = 0
    for state in reachableStates(problem):
        count += 1
        h = heuristic(state, problem)
        if h < 0:
            violations.append('negative h=%s' % h)
        if problem.isGoalState(state) and h != 0:
            violations.append('h=%s at a goal state' % h)
        for successor, _action, cost in problem.getSuccessors(state):
            hNext = heuristic(successor, problem)
            if h > cost + hNext:
                violations.append('inconsistent: h(s)=%s > %s + h(s\')=%s' % (h, cost, hNext))

    # A fresh problem, so the counters and caches above do not matter here.
    fresh = problemClass(loadState(layoutName))
    optimal = fresh.getCostOfActions(search.ucs(fresh))
    hStart = heuristic(fresh.getStartState(), fresh)
    return count, violations, hStart, optimal


CASES = [
    ('Q6 cornersHeuristic', searchAgents.CornersProblem, searchAgents.cornersHeuristic, 'tinyCorners'),
    ('Q6 cornersHeuristic', searchAgents.CornersProblem, searchAgents.cornersHeuristic, 'mediumCorners'),
    ('Q7 foodHeuristic', searchAgents.FoodSearchProblem, searchAgents.foodHeuristic, 'testSearch'),
    ('Q7 foodHeuristic', searchAgents.FoodSearchProblem, searchAgents.foodHeuristic, 'tinySearch'),
]


def main():
    print('%-20s %-14s %8s %8s %8s  %s' % ('Heuristic', 'Layout', 'States', 'h(start)', 'Optimal', 'Result'))
    print('-' * 72)
    allOk = True
    for name, problemClass, heuristic, layoutName in CASES:
        count, violations, hStart, optimal = check(problemClass, heuristic, layoutName)
        ok = not violations and hStart <= optimal
        allOk = allOk and ok
        print('%-20s %-14s %8d %8d %8d  %s' % (name, layoutName, count, hStart, optimal,
                                               'OK' if ok else 'FAILED'))
        for message in violations[:5]:
            print('    ' + message)
    print('-' * 72)
    print('All heuristics admissible and consistent.' if allOk else 'Some checks FAILED.')


if __name__ == '__main__':
    main()
