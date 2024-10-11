# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_series_equal.py
class MySeries(Series):
    pass

s1 = Series([1, 2])
s2 = Series([1, 2])
s3 = MySeries([1, 2])

tm.assert_series_equal(s1, s2, check_series_type=False)
tm.assert_series_equal(s1, s2, check_series_type=True)

tm.assert_series_equal(s1, s3, check_series_type=False)
tm.assert_series_equal(s3, s1, check_series_type=False)

with pytest.raises(AssertionError, match="Series classes are different"):
    tm.assert_series_equal(s1, s3, check_series_type=True)

with pytest.raises(AssertionError, match="Series classes are different"):
    tm.assert_series_equal(s3, s1, check_series_type=True)
