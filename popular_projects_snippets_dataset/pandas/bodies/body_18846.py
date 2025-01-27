# Extracted from ./data/repos/pandas/pandas/_testing/asserters.py
__tracebackhide__ = True
_check_isinstance(left, right, DatetimeArray)

assert_numpy_array_equal(left._ndarray, right._ndarray, obj=f"{obj}._ndarray")
if check_freq:
    assert_attr_equal("freq", left, right, obj=obj)
assert_attr_equal("tz", left, right, obj=obj)
