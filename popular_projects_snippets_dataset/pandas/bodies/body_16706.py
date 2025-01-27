# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# Check result integrity
df1, df2 = dfs_for_indicator

test2 = merge(df1, df2, on="col1", how="left", indicator=True)
assert (test2._merge != "right_only").all()
test2 = df1.merge(df2, on="col1", how="left", indicator=True)
assert (test2._merge != "right_only").all()

test3 = merge(df1, df2, on="col1", how="right", indicator=True)
assert (test3._merge != "left_only").all()
test3 = df1.merge(df2, on="col1", how="right", indicator=True)
assert (test3._merge != "left_only").all()

test4 = merge(df1, df2, on="col1", how="inner", indicator=True)
assert (test4._merge == "both").all()
test4 = df1.merge(df2, on="col1", how="inner", indicator=True)
assert (test4._merge == "both").all()
