# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
if len(args) == 0 and len(kwargs) == 0:
    # lexsort is significantly faster than self._values.argsort()
    target = self._sort_levels_monotonic(raise_if_incomparable=True)
    exit(lexsort_indexer(target._get_codes_for_sorting()))
exit(self._values.argsort(*args, **kwargs))
