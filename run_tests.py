"""Integration test runner for the SE3062 Pac-Man search assignment.

Runs the autograder for each question (Q1-Q7) in its own process, so one
failing question cannot hide the result of another, and prints the score for
each one.

Usage:
    python run_tests.py              # Q1-Q7
    python run_tests.py q4 q5        # only some questions
    python run_tests.py -v           # also print the output of failed questions
"""

import argparse
import re
import subprocess
import sys
import time

QUESTIONS = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7']

TITLES = {
    'q1': 'Depth First Search',
    'q2': 'Breadth First Search',
    'q3': 'Uniform Cost Search',
    'q4': 'A* Search',
    'q5': 'Corners Problem',
    'q6': 'Corners Heuristic',
    'q7': 'Food Heuristic',
}

SCORE_RE = re.compile(r'### Question (q\d+): (\d+)/(\d+) ###')

# The autograder reports node counts in three different formats.
NODES_RES = [
    re.compile(r'nodes expanded:\s+(\d+)'),             # q1-q4 pacman tests
    re.compile(r'expansion of (\d+) nodes'),             # q6 corners heuristic
    re.compile(r'expanded nodes:\s+(\d+)'),             # q7 trickySearch
]


def runQuestion(question):
    """Run the autograder for one question; return (output, seconds taken)."""
    start = time.time()
    result = subprocess.run(
        [sys.executable, 'autograder.py', '-q', question, '--no-graphics'],
        capture_output=True, text=True)
    return result.stdout + result.stderr, time.time() - start


def parseScore(output, question):
    """Return (points, maxPoints) for the question, or None if not found.

    The autograder also runs dependent questions (q5 runs q2 first), so the
    score must be matched by question name, not just taken from the first line.
    """
    for name, points, maxPoints in SCORE_RE.findall(output):
        if name == question:
            return int(points), int(maxPoints)
    return None


def questionSection(output, question):
    """Return only the part of the output that belongs to this question."""
    start = output.find('Question %s\n' % question)
    end = output.find('### Question %s:' % question)
    if start == -1 or end == -1:
        return output
    return output[start:end]


def parseNodes(output, question):
    """Return the node counts the autograder printed for the question."""
    section = questionSection(output, question)
    nodes = []
    for pattern in NODES_RES:
        nodes.extend(int(n) for n in pattern.findall(section))
    return nodes


def printSummary(results):
    """Print one row per question and a total line."""
    print('%-4s %-22s %-7s %-6s %-6s %s' % ('Q', 'Problem', 'Score', 'Status', 'Time', 'Nodes expanded'))
    print('-' * 72)
    totalPoints = totalMax = 0
    for question, score, nodes, seconds in results:
        timeText = '%.1fs' % seconds
        if score is None:
            print('%-4s %-22s %-7s %-6s %-6s' % (question, TITLES[question], '-', 'ERROR', timeText))
            continue
        points, maxPoints = score
        totalPoints += points
        totalMax += maxPoints
        status = 'PASS' if points >= maxPoints else 'FAIL'
        nodeText = ', '.join(str(n) for n in nodes) if nodes else '-'
        print('%-4s %-22s %-7s %-6s %-6s %s' % (question, TITLES[question],
                                                '%d/%d' % (points, maxPoints), status,
                                                timeText, nodeText))
    print('-' * 72)
    print('Total: %d/%d' % (totalPoints, totalMax))


def parseArgs():
    parser = argparse.ArgumentParser(description='Run the autograder for Q1-Q7.')
    parser.add_argument('questions', nargs='*', default=QUESTIONS, metavar='qN',
                        help='questions to run (default: q1 to q7)')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='print the full autograder output for failed questions')
    args = parser.parse_args()
    unknown = [q for q in args.questions if q not in TITLES]
    if unknown:
        parser.error('unknown question(s): %s' % ', '.join(unknown))
    return args


def main():
    args = parseArgs()
    results = []
    failedOutputs = []
    for question in args.questions:
        output, seconds = runQuestion(question)
        score = parseScore(output, question)
        results.append((question, score, parseNodes(output, question), seconds))
        if score is None or score[0] < score[1]:
            failedOutputs.append((question, output))
    printSummary(results)

    if args.verbose:
        for question, output in failedOutputs:
            print('\n===== %s output =====' % question)
            print(output)

    # Non-zero exit code if any question did not get full marks, so the
    # script can be used before merging a pull request.
    sys.exit(1 if failedOutputs else 0)


if __name__ == '__main__':
    main()
