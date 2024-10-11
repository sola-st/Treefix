# Extracted from ./data/repos/pandas/pandas/tests/util/test_hashing.py
# GH#28969 array containing a tuple raises on call to arr.astype(str)
#  apparently a numpy bug github.com/numpy/numpy/issues/9441

df = DataFrame({"data": data})
result = hash_pandas_object(df)
expected = Series(result_data, dtype=np.uint64)
tm.assert_series_equal(result, expected)
