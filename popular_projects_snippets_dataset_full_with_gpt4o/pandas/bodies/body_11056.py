# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
# GH 47985
empty_df = DataFrame({"a": [], "b": []})
gb = empty_df.groupby("a", group_keys=True)
group = getattr(gb, "b")

result = getattr(group, method)(op)
expected = Series(
    [], name="b", dtype="float64", index=Index([], dtype="float64", name="a")
)

tm.assert_series_equal(result, expected)
