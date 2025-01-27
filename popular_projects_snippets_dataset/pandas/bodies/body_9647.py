# Extracted from ./data/repos/pandas/pandas/tests/arrays/numpy_/test_numpy.py
# don't raise when calling factorize on unsigned int PandasArray
arr = np.array([1, 2, 3], dtype=np.uint64)
obj = PandasArray(arr)

res_codes, res_unique = obj.factorize()
exp_codes, exp_unique = pd.factorize(arr)

tm.assert_numpy_array_equal(res_codes, exp_codes)

tm.assert_extension_array_equal(res_unique, PandasArray(exp_unique))
