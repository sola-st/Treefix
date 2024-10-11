# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply_relabeling.py
# this is to test there is no duplicated method used in agg
df = pd.DataFrame({"A": [1, 2, 1, 2], "B": [1, 2, 3, 4]})

result = df["A"].agg(foo="sum")
expected = df["A"].agg({"foo": "sum"})
tm.assert_series_equal(result, expected)

result = df["B"].agg(foo="min", bar="max")
expected = df["B"].agg({"foo": "min", "bar": "max"})
tm.assert_series_equal(result, expected)

result = df["B"].agg(foo=sum, bar=min, cat="max")
expected = df["B"].agg({"foo": sum, "bar": min, "cat": "max"})
tm.assert_series_equal(result, expected)
