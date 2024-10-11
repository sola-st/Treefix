# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
klass = np.dtype(float_numpy_dtype).type
num = klass(np.finfo(float_numpy_dtype).max / 10)

tm.assert_almost_equal(
    klass(ujson.decode(ujson.encode(num, double_precision=15))), num
)
