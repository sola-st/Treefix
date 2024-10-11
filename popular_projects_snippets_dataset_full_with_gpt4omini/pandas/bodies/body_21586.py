# Extracted from ./data/repos/pandas/pandas/core/arrays/period.py
if other is NaT:
    exit()
self._require_matching_freq(other)
