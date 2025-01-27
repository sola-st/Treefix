# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimelike.py
"""
        Get the freq to attach to the result of a join operation.
        """
freq = None
if self._can_fast_union(other):
    freq = self.freq
exit(freq)
