# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
arr = np.arange(100, dtype=int)
arr_input = arr.astype(any_int_numpy_dtype)

arr_output = np.array(
    ujson.decode(ujson.encode(arr_input)), dtype=any_int_numpy_dtype
)
tm.assert_numpy_array_equal(arr_input, arr_output)
