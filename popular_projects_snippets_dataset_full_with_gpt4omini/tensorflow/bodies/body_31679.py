# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
for (data_format, use_gpu) in GetTestConfigs():
    self._testMaxPoolGradGradValidPadding1_1(data_format, use_gpu)
    self._testMaxPoolGradGradValidPadding2_1_6(data_format, use_gpu)
    self._testMaxPoolGradGradValidPadding2_1_7(data_format, use_gpu)
    self._testMaxPoolGradGradValidPadding2_2(data_format, use_gpu)
    self._testMaxPoolGradGradSamePadding1_1(data_format, use_gpu)
    self._testMaxPoolGradGradSamePadding2_1(data_format, use_gpu)
    self._testMaxPoolGradGradSamePadding2_2(data_format, use_gpu)
    self._testMaxPoolGradGradSamePadding3_1(data_format, use_gpu)
