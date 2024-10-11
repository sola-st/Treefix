# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
# reductions with named functions
result = string_series.agg(["sum", "mean"])
expected = Series(
    [string_series.sum(), string_series.mean()],
    ["sum", "mean"],
    name=string_series.name,
)
tm.assert_series_equal(result, expected)
