# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
# GH 31441
df = DataFrame(["A", "A", "B", "B"], columns=["groups"])
result = df.groupby("groups").apply(function)
expected = Series(expected_values, index=Index(["A", "B"], name="groups"))
tm.assert_series_equal(result, expected)
