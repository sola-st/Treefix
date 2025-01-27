# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
arr = np.arange(12.5, 185.72, 1.7322, dtype=float)
float_input = arr.astype(float_numpy_dtype)

float_output = np.array(
    ujson.decode(ujson.encode(float_input, double_precision=15)),
    dtype=float_numpy_dtype,
)
tm.assert_almost_equal(float_input, float_output)
