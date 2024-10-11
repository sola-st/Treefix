# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/reduce_join_op_test.py
with self.cached_session():
    inputs = np.zeros([0, 1], dtype=str)

    # Reduction that drops the dim of size 0.
    output = string_ops.reduce_join(inputs=inputs, axis=0)
    self.assertAllEqualUnicode([""], self.evaluate(output))

    # Reduction that keeps the dim of size 0.
    output = string_ops.reduce_join(inputs=inputs, axis=1)
    output_shape = self.evaluate(output).shape
    self.assertAllEqual([0], output_shape)
