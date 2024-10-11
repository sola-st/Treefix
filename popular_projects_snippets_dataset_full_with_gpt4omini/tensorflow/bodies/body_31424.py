# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
expected_output = [
    14.0, 32.0, 50.0, 100.0, 163.0, 226.0, 167.0, 212.0, 257.0, 122.0,
    140.0, 158.0, 478.0, 541.0, 604.0, 437.0, 482.0, 527.0
]
for (data_format, use_gpu) in GetTestConfigs():
    # The GPU version of this test is not very stable. So adjusting the
    # error threshold to 1e-4.
    self._RunAndVerifyBackpropInput(
        input_sizes=[1, 2, 3, 3],
        filter_sizes=[2, 2, 3, 3],
        output_sizes=[1, 1, 2, 3],
        strides=[1, 1],
        padding="VALID",
        expected=expected_output,
        data_format=data_format,
        use_gpu=use_gpu,
        err=1e-4)
