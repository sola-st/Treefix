# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_copy.py
# GH#47878
idx = MultiIndex(
    levels=[["foo", "bar"], ["fizz", "buzz"]],
    codes=[[0, 0, 0, 1], [0, 0, 1, 1]],
    names=["first", "second"],
)

res = idx.copy(deep=False)
assert res._id is idx._id
