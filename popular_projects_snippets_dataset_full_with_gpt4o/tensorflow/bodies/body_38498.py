# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/argmax_op_test.py
x = np.asarray(100 * np.random.randn(200), dtype=np.float32)
expected_values = x.argmax()
with self.session():
    ans = math_ops.argmax(x, axis=0, output_type=dtypes.int32)
    tf_ans = self.evaluate(ans)
    self.assertEqual(np.int32, tf_ans.dtype)
    # The values are equal when comparing int32 to int64 because
    # the values don't have a range that exceeds 32-bit integers.
    self.assertAllEqual(tf_ans, expected_values)
expected_values = x.argmin()
with self.session():
    ans = math_ops.argmin(x, axis=0, output_type=dtypes.int32)
    tf_ans = self.evaluate(ans)
    self.assertEqual(np.int32, tf_ans.dtype)
    self.assertAllEqual(tf_ans, expected_values)
