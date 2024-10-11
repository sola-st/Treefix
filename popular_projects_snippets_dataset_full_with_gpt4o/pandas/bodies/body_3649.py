# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reorder_levels.py
index = MultiIndex(
    levels=[["bar"], ["one", "two", "three"], [0, 1]],
    codes=[[0, 0, 0, 0, 0, 0], [0, 1, 2, 0, 1, 2], [0, 1, 0, 1, 0, 1]],
    names=["L0", "L1", "L2"],
)
df = DataFrame({"A": np.arange(6), "B": np.arange(6)}, index=index)
obj = tm.get_obj(df, frame_or_series)

# no change, position
result = obj.reorder_levels([0, 1, 2])
tm.assert_equal(obj, result)

# no change, labels
result = obj.reorder_levels(["L0", "L1", "L2"])
tm.assert_equal(obj, result)

# rotate, position
result = obj.reorder_levels([1, 2, 0])
e_idx = MultiIndex(
    levels=[["one", "two", "three"], [0, 1], ["bar"]],
    codes=[[0, 1, 2, 0, 1, 2], [0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0]],
    names=["L1", "L2", "L0"],
)
expected = DataFrame({"A": np.arange(6), "B": np.arange(6)}, index=e_idx)
expected = tm.get_obj(expected, frame_or_series)
tm.assert_equal(result, expected)

result = obj.reorder_levels([0, 0, 0])
e_idx = MultiIndex(
    levels=[["bar"], ["bar"], ["bar"]],
    codes=[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],
    names=["L0", "L0", "L0"],
)
expected = DataFrame({"A": np.arange(6), "B": np.arange(6)}, index=e_idx)
expected = tm.get_obj(expected, frame_or_series)
tm.assert_equal(result, expected)

result = obj.reorder_levels(["L0", "L0", "L0"])
tm.assert_equal(result, expected)
