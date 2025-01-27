# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_setops.py
# GH#38323
mi = MultiIndex.from_tuples([], names=["a", "b"])
mi2 = MultiIndex.from_tuples([data], names=names)
result = mi._maybe_match_names(mi2)
assert result == expected
