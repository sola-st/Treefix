# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_3d_test.py
expected_results = []
computed_results = []
default_dilations = (
    dilations[0] == 1 and dilations[1] == 1 and dilations[2] == 1)
for data_format, use_gpu in GetTestConfigs():
    # If any dilation rate is larger than 1, only do test on the GPU
    # because we currently do not have a CPU implementation for arbitrary
    # dilation rates.
    if default_dilations or use_gpu:
        expected, computed = self._ComputeReferenceDilatedConv(
            tensor_in_sizes, filter_in_sizes, stride, dilations, padding,
            data_format, use_gpu)
        expected_results.append(expected)
        computed_results.append(computed)
        tolerance = 1e-2 if use_gpu else 1e-5
        with self.cached_session() as sess:
            expected_values = self.evaluate(expected_results)
            computed_values = self.evaluate(computed_results)
            for e_value, c_value in zip(expected_values, computed_values):
                print("expected = ", e_value)
                print("actual = ", c_value)
                self.assertAllClose(
                    e_value.flatten(), c_value.flatten(), atol=tolerance, rtol=1e-6)
