# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/bucketize_op_test.py
op = math_ops._bucketize(
    array_ops.zeros([0, 3], dtype=dtypes.float32), boundaries=[])
expected_out = np.zeros([0, 3], dtype=np.float32)
with self.session():
    self.assertAllEqual(expected_out, self.evaluate(op))
