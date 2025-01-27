# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH 22160
# nan is special, because from " a is b" doesn't follow "a == b"
# at least, isin() should follow python's "np.nan in [nan] == True"
# casting to -> np.float64 -> another float-object somewhere on
# the way could lead jepardize this behavior
comps = [np.nan]  # could be casted to float64
values = [np.nan]
expected = np.array([True])
result = algos.isin(comps, values)
tm.assert_numpy_array_equal(expected, result)
