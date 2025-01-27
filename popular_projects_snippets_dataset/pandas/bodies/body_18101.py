# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_series_equal.py
# https://github.com/pandas-dev/pandas/issues/32747
left = Series([pd.Interval(0, 1)], dtype="interval")
right = left.astype(object)

msg = """Attributes of Series are different

Attribute "dtype" are different
\\[left\\]:  interval\\[int64, right\\]
\\[right\\]: object"""

tm.assert_series_equal(left, right, check_dtype=False)

with pytest.raises(AssertionError, match=msg):
    tm.assert_series_equal(left, right, check_dtype=True)
