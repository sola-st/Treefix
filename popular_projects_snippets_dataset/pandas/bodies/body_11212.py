# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH 50347
df = DataFrame({"groupby_col": 1, "bool": [True] * n})
df["bool"] = df["bool"].eq(True)
result = df.groupby("groupby_col").sum()
expected = DataFrame({"bool": [n]}, index=Index([1], name="groupby_col"))
tm.assert_frame_equal(result, expected)
