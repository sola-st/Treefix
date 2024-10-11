# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/morphological_ops_test.py
for use_gpu in True, False:
    self._testDilationGradDeterminismError(use_gpu, dtype)
    self._testDilationGradValidPadding_1x1x1(use_gpu, dtype)
    self._testDilationGradSamePadding_1x1x1(use_gpu, dtype)
    self._testDilationGradSamePadding_1x1x2(use_gpu, dtype)
    self._testDilationGradValidPadding_2x2x1(use_gpu, dtype)
    self._testDilationGradSamePadding_2x2x1(use_gpu, dtype)
    self._testDilationGradSamePaddingBatch_2x2x1(use_gpu, dtype)
    self._testDilationGradSamePadding_2x2x4(use_gpu, dtype)
