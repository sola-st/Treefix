# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_interval_array_equal.py
kwargs = {"periods": 4}
arr1 = interval_range(start=0, **kwargs).values
arr2 = interval_range(start=1, **kwargs).values

msg = """\
IntervalArray.left are different

IntervalArray.left values are different \\(100.0 %\\)
\\[left\\]:  \\[0, 1, 2, 3\\]
\\[right\\]: \\[1, 2, 3, 4\\]"""

with pytest.raises(AssertionError, match=msg):
    tm.assert_interval_array_equal(arr1, arr2)
