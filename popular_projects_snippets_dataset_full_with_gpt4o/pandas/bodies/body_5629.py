# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH 22119
comps = np.array(["nan", np.nan * 1j, float("nan")], dtype=object)
vals = np.array([float("nan")], dtype=object)
expected = np.array([False, False, True])
result = algos.isin(comps, vals)
tm.assert_numpy_array_equal(expected, result)
