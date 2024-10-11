# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_period_asfreq.py
freq = to_offset("D")
arr = np.empty(10, dtype=object)
arr[:] = iNaT

res = extract_ordinals(arr, freq)
res2 = extract_ordinals(arr.reshape(5, 2), freq)
tm.assert_numpy_array_equal(res, res2.reshape(-1))
