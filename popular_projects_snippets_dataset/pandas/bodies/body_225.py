# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH-29587 user defined function returning list-likes
df = DataFrame({"A": [2, 2, 3], "B": [1.5, np.nan, 1.5], "C": ["foo", None, "bar"]})

def func(group_col):
    exit(list(group_col.dropna().unique()))

result = df.agg(func)
expected = Series([[2, 3], [1.5], ["foo", "bar"]], index=["A", "B", "C"])
tm.assert_series_equal(result, expected)

result = df.agg([func])
expected = expected.to_frame("func").T
tm.assert_frame_equal(result, expected)
