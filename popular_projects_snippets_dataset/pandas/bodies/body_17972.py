# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_interval_array_equal.py
kwargs = {"start": 0}
arr1 = interval_range(periods=5, **kwargs).values
arr2 = interval_range(periods=6, **kwargs).values

msg = """\
IntervalArray.left are different

IntervalArray.left shapes are different
\\[left\\]:  \\(5,\\)
\\[right\\]: \\(6,\\)"""

with pytest.raises(AssertionError, match=msg):
    tm.assert_interval_array_equal(arr1, arr2)
