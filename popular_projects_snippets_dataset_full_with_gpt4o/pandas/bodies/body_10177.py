# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
# GH 39732
g = roll_frame.groupby("A", group_keys=False)
expected = g.apply(lambda x: x.rolling(4).sum()).index
_ = g.rolling(window=4)
result = g.apply(lambda x: x.rolling(4).sum()).index
tm.assert_index_equal(result, expected)
assert not g.mutated
assert not g.grouper.mutated
