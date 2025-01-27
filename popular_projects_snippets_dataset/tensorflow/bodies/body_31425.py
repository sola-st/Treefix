# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
expected_output = [
    1.0, 2.0, 2.0, 4.0, 3.0, 6.0, 7.0, 12.0, 11.0, 18.0, 15.0, 24.0, 12.0,
    16.0, 15.0, 20.0, 18.0, 24.0
]
for (data_format, use_gpu) in GetTestConfigs():
    self._RunAndVerifyBackpropInput(
        input_sizes=[1, 3, 6, 1],
        filter_sizes=[2, 2, 1, 1],
        output_sizes=[1, 2, 3, 1],
        strides=[1, 2],
        padding="VALID",
        expected=expected_output,
        data_format=data_format,
        use_gpu=use_gpu,
        err=1e-5)
