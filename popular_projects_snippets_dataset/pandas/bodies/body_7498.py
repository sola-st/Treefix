# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_copy.py
idx = MultiIndex(
    levels=[["foo", "bar"], ["fizz", "buzz"]],
    codes=[[0, 0, 0, 1], [0, 0, 1, 1]],
    names=["first", "second"],
)
idx_copy = idx.copy(deep=deep)
assert idx_copy.equals(idx)
