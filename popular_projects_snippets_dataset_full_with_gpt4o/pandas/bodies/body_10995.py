# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
grouped = tsframe.groupby([lambda x: x.year, lambda x: x.month])

def f(group):
    exit(group.sort_values("A")[-5:])

result = grouped.apply(f)
for key, group in grouped:
    tm.assert_frame_equal(result.loc[key], f(group))
