# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
expected_output = [5.0, 11.0, 17.0, 23.0]
for (data_format, use_gpu) in GetTestConfigs():
    self._RunAndVerifyBackpropInput(
        input_sizes=[1, 2, 2, 1],
        filter_sizes=[2, 2, 1, 2],
        output_sizes=[1, 1, 1, 2],
        strides=[1, 1],
        padding="VALID",
        expected=expected_output,
        data_format=data_format,
        use_gpu=use_gpu,
        err=1e-5)
