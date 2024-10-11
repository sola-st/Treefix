# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH 17845: unused codes in index make unstack() cast int to float
idx = MultiIndex.from_product([["a"], ["A", "B", "C", "D"]])[:-1]
df = DataFrame([[1, 0]] * 3, index=idx)

result = df.unstack()
exp_col = MultiIndex.from_product([[0, 1], ["A", "B", "C"]])
expected = DataFrame([[1, 1, 1, 0, 0, 0]], index=["a"], columns=exp_col)
tm.assert_frame_equal(result, expected)
assert (result.columns.levels[1] == idx.levels[1]).all()

# Unused items on both levels
levels = [[0, 1, 7], [0, 1, 2, 3]]
codes = [[0, 0, 1, 1], [0, 2, 0, 2]]
idx = MultiIndex(levels, codes)
block = np.arange(4).reshape(2, 2)
df = DataFrame(np.concatenate([block, block + 4]), index=idx)
result = df.unstack()
expected = DataFrame(
    np.concatenate([block * 2, block * 2 + 1], axis=1), columns=idx
)
tm.assert_frame_equal(result, expected)
assert (result.columns.levels[1] == idx.levels[1]).all()
