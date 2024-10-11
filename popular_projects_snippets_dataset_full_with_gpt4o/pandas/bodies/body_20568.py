# Extracted from ./data/repos/pandas/pandas/core/indexes/interval.py
# Note: we _could_ use libjoin functions by either casting to object
#  dtype or constructing tuples (faster than constructing Intervals)
#  but the libjoin fastpaths are no longer fast in these cases.
raise NotImplementedError(
    "IntervalIndex does not use libjoin fastpaths or pass values to "
    "IndexEngine objects"
)
