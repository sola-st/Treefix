# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
# GH 31248
df = DataFrame({"group": [1, 1, 2], "value": [0, 1, 0]}, index=index)
result = df.groupby("group", group_keys=False).apply(lambda x: x)
tm.assert_frame_equal(result, df)
