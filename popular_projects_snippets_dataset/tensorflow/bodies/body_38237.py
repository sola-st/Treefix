# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/bincount_op_test.py
arr = np.random.randint(0, 1000, size=1000)
with test_util.deterministic_ops(), self.assertRaisesRegex(
    errors_impl.UnimplementedError,
    "Determinism is not yet supported in GPU implementation of Bincount."):
    self.evaluate(bincount_ops.bincount(arr, None, axis=None))
arr = np.random.randint(0, 1000, size=(100, 100))
with test_util.deterministic_ops(), self.assertRaisesRegex(
    errors_impl.UnimplementedError,
    "Determinism is not yet supported in GPU implementation of "
    "DenseBincount."):
    self.evaluate(bincount_ops.bincount(arr, None, axis=-1))
