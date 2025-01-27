# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
expected_output = []
for (data_format, use_gpu) in GetTestConfigs():
    self._RunAndVerifyBackpropInput(
        input_sizes=[0, 2, 3, 1],
        filter_sizes=[2, 2, 1, 1],
        output_sizes=[0, 1, 2, 1],
        strides=[1, 1],
        padding="VALID",
        expected=expected_output,
        data_format=data_format,
        use_gpu=use_gpu,
        err=1e-5)
