"""
Problem Statement: http://community.topcoder.com/stat?c=problem_statement&pm=12516
"""


class SubstringReversal:
    def solve(self, s):
        for x in range(len(s)):
            for y in range(x + 1, len(s)):
                minY = min(s[y:])
                if s[x] > minY:
                    return [x, s.index(minY, y)]

        return [0, 0]