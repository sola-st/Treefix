# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py

# 8260
# support datetime64 with tz

idx = Index(date_range("20130101", periods=3, tz="US/Eastern"), name="foo")
dr = date_range("20130110", periods=3)

# construction
df = DataFrame({"A": idx, "B": dr})
assert df["A"].dtype, "M8[ns, US/Eastern"
assert df["A"].name == "A"
tm.assert_series_equal(df["A"], Series(idx, name="A"))
tm.assert_series_equal(df["B"], Series(dr, name="B"))
