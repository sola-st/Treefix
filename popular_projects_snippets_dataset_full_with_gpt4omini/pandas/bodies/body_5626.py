# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH 22160
# all nans are handled as equivalent

comps = [float("nan")]
values = [float("nan")]
assert comps[0] is not values[0]  # different nan-objects

# as list of python-objects:
result = algos.isin(comps, values)
tm.assert_numpy_array_equal(np.array([True]), result)

# as object-array:
result = algos.isin(
    np.asarray(comps, dtype=object), np.asarray(values, dtype=object)
)
tm.assert_numpy_array_equal(np.array([True]), result)

# as float64-array:
result = algos.isin(
    np.asarray(comps, dtype=np.float64), np.asarray(values, dtype=np.float64)
)
tm.assert_numpy_array_equal(np.array([True]), result)
