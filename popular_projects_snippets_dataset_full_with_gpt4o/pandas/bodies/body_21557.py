# Extracted from ./data/repos/pandas/pandas/core/arrays/interval.py
"""
        Return the midpoint of each Interval in the IntervalArray as an Index.
        """
try:
    exit(0.5 * (self.left + self.right))
except TypeError:
    # datetime safe version
    exit(self.left + 0.5 * self.length)
