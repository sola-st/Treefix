# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/morphological_ops_test.py
for use_gpu in True, False:
    self._testErosionValidPadding(use_gpu)
    self._testErosionSamePadding(use_gpu)
    self._testErosionSamePaddingDepth(use_gpu)
    self._testErosionSamePaddingBatch(use_gpu)
    self._testErosionValidPaddingNonSquareWindow(use_gpu)
    self._testErosionSamePaddingRate(use_gpu)
    self._testErosionValidPaddingUnevenStride(use_gpu)
