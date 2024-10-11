# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# With mixed dtype and NaN
levels = [["a", 2, "c"], [1, 3, 5, 7]]
codes = [[0, -1, 1, 1], [0, 2, -1, 2]]
idx = MultiIndex(levels, codes)
data = np.arange(8)
df = DataFrame(data.reshape(4, 2), index=idx)

result = df.unstack(level=level)
exp_data = np.zeros(18) * np.nan
exp_data[idces] = data
cols = MultiIndex.from_product([[0, 1], col_level])
expected = DataFrame(exp_data.reshape(3, 6), index=idx_level, columns=cols)
tm.assert_frame_equal(result, expected)
