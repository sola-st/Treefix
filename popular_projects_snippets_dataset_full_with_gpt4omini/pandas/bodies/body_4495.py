# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# from #1074
d = DataFrame({"a": [np.nan, False]})
assert d["a"].dtype == np.object_
assert not d["a"][1]
