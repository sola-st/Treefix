# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_equals.py
# GH#37667 Case where other contains a value not among ci's
#  categories ("D") and also contains np.nan
ci = CategoricalIndex(["A", "B", np.nan, np.nan])
other = Index(["A", "B", "D", np.nan])

assert not ci.equals(other)
