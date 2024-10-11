# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
bfloat16 = dtypes_lib.bfloat16.as_numpy_dtype
x = np.linspace(-20, 20, 10).reshape(1, 2, 5).astype(bfloat16)  # pylint: disable=too-many-function-args
# y cannot be zero
y = np.linspace(-20, 20, 10).reshape(1, 2, 5).astype(bfloat16)  # pylint: disable=too-many-function-args
self._compareCpu(x, y, np.true_divide, math_ops.xdivy)
self._compareCpu(x, y, np_xlogy, math_ops.xlogy)
self._compareCpu(x, y, np_xlog1py, math_ops.xlog1py)
