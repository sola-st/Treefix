# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
# GH 31223
df = DataFrame({"group": [1, 1, 2], "value": [0, 1, 0]}, index=index)
result = df.groupby("group").agg({"value": Series.nunique})
expected = DataFrame({"group": [1, 2], "value": [2, 1]}).set_index("group")
tm.assert_frame_equal(result, expected)
