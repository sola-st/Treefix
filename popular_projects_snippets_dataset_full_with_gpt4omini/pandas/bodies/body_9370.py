# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_comparison.py
# GH 28930
op_name = f"__{comparison_op.__name__}__"
s1 = pd.Series([1, None, 3], dtype=dtype)
s2 = pd.Series([1, None, 3], dtype="float")

method = getattr(s1, op_name)
result = method(2)

method = getattr(s2, op_name)
expected = method(2).astype("boolean")
expected[s2.isna()] = pd.NA

self.assert_series_equal(result, expected)
