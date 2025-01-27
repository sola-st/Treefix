# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH#16323
# deep check for 1-row case
columns = MultiIndex(levels=levels, codes=[[0, 0, 1, 1], [0, 1, 0, 1]])
df = DataFrame(columns=columns, data=[range(4)])
df_stacked = df.stack(stack_lev)
assert all(
    df.loc[row, col]
    == df_stacked.loc[(row, col[stack_lev]), col[1 - stack_lev]]
    for row in df.index
    for col in df.columns
)
