# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_cat_accessor.py
# GH#17509
ser = Series([1, 2, 3], name="A").astype("category")
expected = "A"
result = method(ser).name
assert result == expected
