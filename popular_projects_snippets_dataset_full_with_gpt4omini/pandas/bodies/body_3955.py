# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH#16323

# check multi-row case
mi = MultiIndex(
    levels=[["A", "C", "B"], ["B", "A", "C"]],
    codes=[np.repeat(range(3), 3), np.tile(range(3), 3)],
)
df = DataFrame(
    columns=mi, index=range(5), data=np.arange(5 * len(mi)).reshape(5, -1)
)
assert all(
    df.loc[row, col] == df.stack(0).loc[(row, col[0]), col[1]]
    for row in df.index
    for col in df.columns
)
