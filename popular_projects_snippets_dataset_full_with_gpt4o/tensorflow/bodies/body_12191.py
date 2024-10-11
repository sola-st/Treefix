# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clip_ops_test.py
# Simple example
self._testClipTensorByGlobalNorm([[-3.0, 0.0, 0.0], [4.0, 0.0, 0.0]], 4.0,
                                 [[-2.4, 0.0, 0.0], [3.2, 0.0, 0.0]])
# No clipping.
self._testClipTensorByGlobalNorm([[1.0, 0.0, 0.0], [1.0, 0.0, 0.0]], 4.0,
                                 [[1.0, 0.0, 0.0], [1.0, 0.0, 0.0]])
# Zero norm.
self._testClipTensorByGlobalNorm([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], 4.0,
                                 [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
