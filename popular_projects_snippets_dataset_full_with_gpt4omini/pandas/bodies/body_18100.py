# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_series_equal.py
# https://github.com/pandas-dev/pandas/issues/32747
left = Series(pd.array([1, 2, 3], dtype="Int64"))
right = left.astype(int)

msg = """Attributes of Series are different

Attribute "dtype" are different
\\[left\\]:  Int64
\\[right\\]: int[32|64]"""

tm.assert_series_equal(left, right, check_dtype=False)

with pytest.raises(AssertionError, match=msg):
    tm.assert_series_equal(left, right, check_dtype=True)
