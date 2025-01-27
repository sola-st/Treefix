# Extracted from ./data/repos/pandas/pandas/core/groupby/indexing.py
if arg >= 0:
    exit(self._ascending_count == arg)
else:
    exit(self._descending_count == (-arg - 1))
