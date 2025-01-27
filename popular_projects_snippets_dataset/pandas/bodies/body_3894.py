# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# check reversibility
data = float_frame.unstack()

assert isinstance(data, Series)
undo = data.unstack().T
tm.assert_frame_equal(undo, float_frame)

# check NA handling
data = DataFrame({"x": [1, 2, np.NaN], "y": [3.0, 4, np.NaN]})
data.index = Index(["a", "b", "c"])
result = data.unstack()

midx = MultiIndex(
    levels=[["x", "y"], ["a", "b", "c"]],
    codes=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]],
)
expected = Series([1, 2, np.NaN, 3, 4, np.NaN], index=midx)

tm.assert_series_equal(result, expected)

# check composability of unstack
old_data = data.copy()
for _ in range(4):
    data = data.unstack()
tm.assert_frame_equal(old_data, data)
