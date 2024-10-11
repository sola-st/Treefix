# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# GH32146
ind = Index([True, False, np.nan], dtype=object)
exp = np.array([True, False, np.nan], dtype=object)
out = lib.maybe_convert_objects(ind.values, safe=1)
tm.assert_numpy_array_equal(out, exp)
