# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/bucketize_op_test.py
op = math_ops._bucketize(
    constant_op.constant([[-5, 0, 2, 3, 5], [8, 10, 11, 12, 0]]),
    boundaries=[0, 3, 8, 11])
expected_out = [[0, 1, 1, 2, 2], [3, 3, 4, 4, 1]]
with self.session():
    self.assertAllEqual(expected_out, self.evaluate(op))
