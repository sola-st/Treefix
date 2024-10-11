# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
expected_results = []
computed_results = []
for data_format, use_gpu in GetTestConfigs():
    expected, computed = self._ComputeReferenceDilatedConv(
        tensor_in_sizes, filter_in_sizes, strides, dilations, padding,
        data_format, use_gpu)
    expected_results.append(expected)
    computed_results.append(computed)
tolerance = 1e-2 if use_gpu else 1e-5
expected_values = self.evaluate(expected_results)
computed_values = self.evaluate(computed_results)
for e_value, c_value in zip(expected_values, computed_values):
    tf_logging.debug("expected = %s", e_value)
    tf_logging.debug("actual = %s", c_value)
    self.assertAllClose(
        e_value.flatten(), c_value.flatten(), atol=tolerance, rtol=rtol)
