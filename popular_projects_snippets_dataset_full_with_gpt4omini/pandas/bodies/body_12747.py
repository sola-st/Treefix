# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
dtype = np.float32

arr = np.arange(100.202, 200.202, 1, dtype=dtype)
arr = arr.reshape((5, 5, 4))

arr_out = np.array(ujson.decode(ujson.encode(arr)), dtype=dtype)
tm.assert_almost_equal(arr, arr_out)
