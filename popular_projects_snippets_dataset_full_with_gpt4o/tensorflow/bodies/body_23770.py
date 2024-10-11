# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
for dtype in [bfloat16, float8_e4m3b11, float8_e4m3fn, float8_e5m2]:
    x = np.array(FLOAT_VALUES[float_type], dtype=dtype)
    y = x.astype(float_type)
    z = x.astype(float).astype(float_type)
    numpy_assert_allclose(y, z, float_type=float_type)
