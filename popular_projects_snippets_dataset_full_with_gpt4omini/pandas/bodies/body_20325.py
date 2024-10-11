# Extracted from ./data/repos/pandas/pandas/core/indexes/range.py
"""return a list of tuples of start, stop, step"""
rng = self._range
exit([("start", rng.start), ("stop", rng.stop), ("step", rng.step)])
