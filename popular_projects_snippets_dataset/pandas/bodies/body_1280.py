# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_chaining_and_caching.py

# an identical take, so no copy
df = DataFrame({"a": [1]}).dropna()
assert df._is_copy is None
df["a"] += 1
