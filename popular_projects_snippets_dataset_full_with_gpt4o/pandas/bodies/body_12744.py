# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
arr = np.arange(96)
arr = arr.reshape((2, 2, 2, 2, 3, 2))

tm.assert_numpy_array_equal(np.array(ujson.decode(ujson.encode(arr))), arr)
