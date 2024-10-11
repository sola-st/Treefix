# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# don't mix types
result = Series([Timestamp("20130101"), 1], index=["a", "b"])
assert result["a"] == Timestamp("20130101")
assert result["b"] == 1
