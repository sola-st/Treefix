# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
for (data_format, use_gpu) in GetTestConfigs():
    self._testAvgPoolGradValidPadding1_1(data_format, use_gpu)
    self._testAvgPoolGradValidPadding1_2(data_format, use_gpu)
    self._testAvgPoolGradValidPadding2_1(data_format, use_gpu)
    self._testAvgPoolGradValidPadding2_2(data_format, use_gpu)
    self._testAvgPoolGradSamePadding1_1(data_format, use_gpu)
    self._testAvgPoolGradSamePadding1_2(data_format, use_gpu)
    self._testAvgPoolGradSamePadding2_1(data_format, use_gpu)
    self._testAvgPoolGradSamePadding2_2(data_format, use_gpu)
    self._testAvgPoolGradSamePadding3_1(data_format, use_gpu)
