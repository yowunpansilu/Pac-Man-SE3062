"""Integration test runner for the SE3062 Pac-Man search assignment.

Runs the autograder for each question (Q1-Q7) in its own process, so one
failing question cannot hide the result of another, and prints the score for
each one.

Usage:
    python run_tests.py
"""

import re
import subprocess
import sys

QUESTIONS = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7']

SCORE_RE = re.compile(r'### Question (q\d+): (\d+)/(\d+) ###')


def runQuestion(question):
    """Run the autograder for one question and return its full output."""
    result = subprocess.run(
        [sys.executable, 'autograder.py', '-q', question, '--no-graphics'],
        capture_output=True, text=True)
    return result.stdout + result.stderr


def parseScore(output, question):
    """Return (points, maxPoints) for the question, or None if not found.

    The autograder also runs dependent questions (q5 runs q2 first), so the
    score must be matched by question name, not just taken from the first line.
    """
    for name, points, maxPoints in SCORE_RE.findall(output):
        if name == question:
            return int(points), int(maxPoints)
    return None


def main():
    for question in QUESTIONS:
        score = parseScore(runQuestion(question), question)
        if score is None:
            print('%s: no score found (crashed?)' % question)
        else:
            print('%s: %d/%d' % (question, score[0], score[1]))


if __name__ == '__main__':
    main()
