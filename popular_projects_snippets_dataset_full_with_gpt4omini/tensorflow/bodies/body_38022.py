# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
dtypes = [np.float16, np.float32, np.float64, np.int32, np.int64]
funcs = [
    math_ops.less, math_ops.less_equal, math_ops.greater,
    math_ops.greater_equal, math_ops.equal, math_ops.not_equal
]
x = np.arange(0, 10).reshape([2, 5])
y = np.arange(0, 10).reshape([5, 2])
for t in dtypes:
    for f in funcs:
        with self.assertRaisesIncompatibleShapesError(
            (ValueError, errors.InvalidArgumentError)):
            f(x.astype(t), y.astype(t))
