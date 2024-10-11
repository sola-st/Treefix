# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
expected = [
    17.0, 22.0, 27.0, 22.0, 29.0, 36.0, 27.0, 36.0, 45.0, 32.0, 43.0, 54.0,
    37.0, 50.0, 63.0, 42.0, 57.0, 72.0, 62.0, 85.0, 108.0, 67.0, 92.0,
    117.0, 72.0, 99.0, 126.0, 77.0, 106.0, 135.0, 82.0, 113.0, 144.0, 87.0,
    120.0, 153.0
]
for (data_format, use_gpu) in GetTestConfigs():
    self._RunAndVerifyBackpropFilter(
        input_sizes=[1, 2, 3, 3],
        filter_sizes=[2, 2, 3, 3],
        output_sizes=[1, 1, 2, 3],
        strides=[1, 1],
        padding="VALID",
        expected=expected,
        data_format=data_format,
        use_gpu=use_gpu)
