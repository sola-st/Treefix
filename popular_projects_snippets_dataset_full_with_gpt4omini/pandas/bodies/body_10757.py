# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
grouped = tsframe.groupby([lambda x: x.year, lambda x: x.month])
result = grouped.describe()
desc_groups = []
for col in tsframe:
    group = grouped[col].describe()
    # GH 17464 - Remove duplicate MultiIndex levels
    group_col = MultiIndex(
        levels=[[col], group.columns],
        codes=[[0] * len(group.columns), range(len(group.columns))],
    )
    group = DataFrame(group.values, columns=group_col, index=group.index)
    desc_groups.append(group)
expected = pd.concat(desc_groups, axis=1)
tm.assert_frame_equal(result, expected)

groupedT = tsframe.groupby({"A": 0, "B": 0, "C": 1, "D": 1}, axis=1)
result = groupedT.describe()
expected = tsframe.describe().T
# reverting the change from https://github.com/pandas-dev/pandas/pull/35441/
expected.index = MultiIndex(
    levels=[[0, 1], expected.index],
    codes=[[0, 0, 1, 1], range(len(expected.index))],
)
tm.assert_frame_equal(result, expected)
