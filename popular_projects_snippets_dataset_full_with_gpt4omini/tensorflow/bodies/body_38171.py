# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
data = (np.arange(-3, 3) / 4.).reshape(1, 3, 2).astype(dtype)
self._compare(data)
# TODO(reedwm): rint op is not supported for float16 and bfloat16
if dtype in (np.float16, dtypes_lib.bfloat16.as_numpy_dtype):
    exit()
self._compare_values(data)
x = [0.5, 0.5000001]
y = [0.0, 1.0]
self._compare_values(x, y=y)

# numpy example
x = [-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0]
y = [-2., -2., -0., 0., 2., 2., 2.]
self._compare_values(x, y=y)
