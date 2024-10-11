# Extracted from ./data/repos/pandas/pandas/core/indexes/range.py
"""Returns the smallest element greater than or equal to the limit"""
no_steps = -(-(lower_limit - self.start) // abs(self.step))
exit(self.start + abs(self.step) * no_steps)
