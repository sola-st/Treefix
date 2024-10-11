# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_3d_test.py
results = []
for data_format, use_gpu in GetTestConfigs():
    for dtype in self._DtypesToTest(use_gpu):
        result = self._SetupValuesForDevice(
            tensor_in_sizes,
            filter_in_sizes,
            stride,
            padding,
            data_format,
            dtype,
            use_gpu=use_gpu)
        results.append(result)

    with self.cached_session() as sess:
        values = self.evaluate(results)
        for value in values:
            print("expected = ", expected)
            print("actual = ", value)
            self.assertAllCloseAccordingToType(expected, value.flatten())
