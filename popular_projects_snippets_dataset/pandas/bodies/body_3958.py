# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
codes = np.tile(np.arange(500), 2)
level = np.arange(500)

index = MultiIndex(
    levels=[level] * 8 + [[0, 1]],
    codes=[codes] * 8 + [np.arange(2).repeat(500)],
)

s = Series(np.arange(1000), index=index)
result = s.unstack()
assert result.shape == (500, 2)

# test roundtrip
stacked = result.stack()
tm.assert_series_equal(s, stacked.reindex(s.index))

# put it at beginning
index = MultiIndex(
    levels=[[0, 1]] + [level] * 8,
    codes=[np.arange(2).repeat(500)] + [codes] * 8,
)

s = Series(np.arange(1000), index=index)
result = s.unstack(0)
assert result.shape == (500, 2)

# put it in middle
index = MultiIndex(
    levels=[level] * 4 + [[0, 1]] + [level] * 4,
    codes=([codes] * 4 + [np.arange(2).repeat(500)] + [codes] * 4),
)

s = Series(np.arange(1000), index=index)
result = s.unstack(4)
assert result.shape == (500, 2)
