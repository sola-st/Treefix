# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
arr = np.arange(100)
arr = arr.reshape(shape)

tm.assert_numpy_array_equal(np.array(ujson.decode(ujson.encode(arr))), arr)
