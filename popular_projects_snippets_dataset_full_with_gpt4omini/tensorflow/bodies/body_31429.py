# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
input_sizes = [3, 1, 1, 2]
expected_output = np.zeros(input_sizes).flatten()
for (data_format, use_gpu) in GetTestConfigs():
    self._RunAndVerifyBackpropInput(
        input_sizes=input_sizes,
        filter_sizes=[1, 3, 2, 3],
        output_sizes=[3, 1, 0, 3],
        strides=[1, 2],
        padding="VALID",
        expected=expected_output,
        data_format=data_format,
        use_gpu=use_gpu,
        err=1e-5)
