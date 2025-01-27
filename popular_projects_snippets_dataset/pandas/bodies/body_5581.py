# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH35650 Verify whether read-only datetime64 array can be factorized
data = np.array([np.datetime64("2020-01-01T00:00:00.000")])
data.setflags(write=writable)
expected_codes = np.array([0], dtype=np.intp)
expected_uniques = np.array(
    ["2020-01-01T00:00:00.000000000"], dtype="datetime64[ns]"
)

codes, uniques = pd.factorize(data)
tm.assert_numpy_array_equal(codes, expected_codes)
tm.assert_numpy_array_equal(uniques, expected_uniques)
