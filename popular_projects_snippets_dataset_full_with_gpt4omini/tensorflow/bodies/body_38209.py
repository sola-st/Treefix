# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/clip_ops_test.py
values = [[[-3.0, 0.0, 0.0], [4.0, 0.0, 0.0]],
          [[0.0, 2.0, 0.0], [0.0, 0.0, -1.0]]]
indices = [2, 6]
shape = [10, 2, 3]
# [-2.0, 2.0]
self._testClipIndexedSlicesByValue(values, indices, shape, -2.0, 2.0,
                                   [[[-2.0, 0.0, 0.0], [2.0, 0.0, 0.0]],
                                    [[0.0, 2.0, 0.0], [0.0, 0.0, -1.0]]])
# [1.0, 2.0]
self._testClipIndexedSlicesByValue(values, indices, shape, 1.0, 2.0,
                                   [[[1.0, 1.0, 1.0], [2.0, 1.0, 1.0]],
                                    [[1.0, 2.0, 1.0], [1.0, 1.0, 1.0]]])
# [-2.0, -1.0]
self._testClipIndexedSlicesByValue(
    values, indices, shape, -2.0, -1.0,
    [[[-2.0, -1.0, -1.0], [-1.0, -1.0, -1.0]],
     [[-1.0, -1.0, -1.0], [-1.0, -1.0, -1.0]]])
