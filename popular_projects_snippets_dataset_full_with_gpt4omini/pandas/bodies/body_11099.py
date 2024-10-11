# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH 38815
grouped = df.groupby("A")
result = getattr(grouped, agg_function)()
expected = result.copy()
expected.loc["bar", "B"] = getattr(df.loc[df["A"] == "bar", "B"], agg_function)()
expected.loc["foo", "B"] = getattr(df.loc[df["A"] == "foo", "B"], agg_function)()
tm.assert_frame_equal(result, expected)
