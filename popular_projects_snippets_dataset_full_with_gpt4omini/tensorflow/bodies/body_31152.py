# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/morphological_ops_test.py
for use_gpu in True, False:
    self._testErosionGradValidPadding_1x1x1(use_gpu)
    self._testErosionGradSamePadding_1x1x1(use_gpu)
    self._testErosionGradSamePadding_1x1x2(use_gpu)
    self._testErosionGradValidPadding_2x2x1(use_gpu)
    self._testErosionGradSamePadding_2x2x1(use_gpu)
    self._testErosionGradSamePaddingBatch_2x2x1(use_gpu)
    self._testErosionGradSamePadding_2x2x4(use_gpu)
