# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
for dtype in [
    np.float16, np.float32, np.float64, dtypes.bfloat16.as_numpy_dtype,
    np.int32, np.int64
]:
    x = np.array([[1, 2, 3], [4, 5, 6]], dtype=dtype)
    y = np.array([-3, -2, -1], dtype=dtype)
    z = (x - y) * (x - y)
    with test_util.device(use_gpu=True):
        z_tf = self.evaluate(math_ops.squared_difference(x, y))
        self.assertAllClose(z, z_tf)
