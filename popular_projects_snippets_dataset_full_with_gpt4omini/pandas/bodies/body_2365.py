# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_xs.py
# GH#35301

index = MultiIndex(
    levels=[[("foo", "bar", 0), ("foo", "baz", 0), ("foo", "qux", 0)], [0, 1]],
    codes=[[0, 0, 1, 1, 2, 2], [0, 1, 0, 1, 0, 1]],
)

obj = DataFrame(np.random.randn(6, 4), index=index)
if frame_or_series is Series:
    obj = obj[0]

expected = obj.iloc[-2:].droplevel(0)

result = obj.xs(IndexSlice[("foo", "qux", 0), :])
tm.assert_equal(result, expected)

result = obj.loc[IndexSlice[("foo", "qux", 0), :]]
tm.assert_equal(result, expected)
