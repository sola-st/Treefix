# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
# demonstration tests
s = Series(range(6), dtype="int64", name="series")

result = s.agg(["min", "max"])
expected = Series([0, 5], index=["min", "max"], name="series")
tm.assert_series_equal(result, expected)

result = s.agg({"foo": "min"})
expected = Series([0], index=["foo"], name="series")
tm.assert_series_equal(result, expected)
