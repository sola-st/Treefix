# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_interval_array_equal.py
kwargs = {"start": 0, "periods": 5}
arr1 = interval_range(closed="left", **kwargs).values
arr2 = interval_range(closed="right", **kwargs).values

msg = """\
IntervalArray are different

Attribute "closed" are different
\\[left\\]:  left
\\[right\\]: right"""

with pytest.raises(AssertionError, match=msg):
    tm.assert_interval_array_equal(arr1, arr2)
