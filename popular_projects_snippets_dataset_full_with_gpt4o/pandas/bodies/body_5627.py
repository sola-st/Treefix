# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH 22160
# ensure 42 is not casted to a string
comps = ["ss", 42]
values = ["42"]
expected = np.array([False, False])
result = algos.isin(comps, values)
tm.assert_numpy_array_equal(expected, result)
