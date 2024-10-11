# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_view.py

dti = date_range("2016-01-01", periods=3)

orig = box(dti)
obj = orig.view(first)
assert obj.dtype == first
tm.assert_numpy_array_equal(np.asarray(obj.view("i8")), dti.asi8)

res = obj.view(second)
assert res.dtype == second
tm.assert_numpy_array_equal(np.asarray(obj.view("i8")), dti.asi8)
