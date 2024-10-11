# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/nth_element_op_test.py
np_expected_values = np.array(expected_values)
with self.cached_session(use_gpu=False) as sess:
    inputs_op = ops.convert_to_tensor(inputs, dtype=dtype)
    values_op = nn_ops.nth_element(inputs_op, n, reverse=reverse)
    values = self.evaluate(values_op)

    self.assertShapeEqual(np_expected_values, values_op)
    self.assertAllClose(np_expected_values, values)
