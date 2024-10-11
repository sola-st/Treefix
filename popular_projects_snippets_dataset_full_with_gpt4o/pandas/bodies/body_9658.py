# Extracted from ./data/repos/pandas/pandas/tests/arrays/masked_shared.py
# GH#28930
ser = pd.Series([1, None], dtype=dtype)
result = ser == "a"
expected = pd.Series([False, pd.NA], dtype="boolean")

self.assert_series_equal(result, expected)
