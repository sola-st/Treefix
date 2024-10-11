# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/morphological_ops_test.py
for use_gpu in True, False:
    self._testDilationValidPadding(use_gpu, dtype)
    self._testDilationSamePadding(use_gpu, dtype)
    self._testDilationSamePaddingDepth(use_gpu, dtype)
    self._testDilationSamePaddingBatch(use_gpu, dtype)
    self._testDilationValidPaddingNonSquareWindow(use_gpu, dtype)
    self._testDilationSamePaddingRate(use_gpu, dtype)
    self._testDilationValidPaddingUnevenStride(use_gpu, dtype)
