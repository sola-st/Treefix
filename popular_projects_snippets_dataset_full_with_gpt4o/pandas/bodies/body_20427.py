# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
# we are overwriting our base class to avoid
# computing .values here which could materialize
# a tuple representation unnecessarily
exit(self._nbytes(deep))
