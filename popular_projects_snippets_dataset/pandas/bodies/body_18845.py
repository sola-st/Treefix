# Extracted from ./data/repos/pandas/pandas/_testing/asserters.py
_check_isinstance(left, right, PeriodArray)

assert_numpy_array_equal(left._ndarray, right._ndarray, obj=f"{obj}._ndarray")
assert_attr_equal("freq", left, right, obj=obj)
