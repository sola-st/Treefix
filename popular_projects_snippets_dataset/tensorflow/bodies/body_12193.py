# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clip_ops_test.py
values = [[[-3.0, 0.0, 0.0], [4.0, 0.0, 0.0]],
          [[0.0, 2.0, 0.0], [0.0, 0.0, -1.0]]]
indices = [2, 6]
shape = [10, 2, 3]
# Axes == None
self._testClipIndexedSlicesByNorm(values, indices, shape, 4.0, None)

# Axes == 0
self._testClipIndexedSlicesByNorm(values, indices, shape, 4.0, 0)

# Axes == 1
self._testClipIndexedSlicesByNorm(values, indices, shape, 4.0, 1)

# Axes == 2
self._testClipIndexedSlicesByNorm(values, indices, shape, 4.0, 1)

# Axes == [0, 1]
self._testClipIndexedSlicesByNorm(values, indices, shape, 4.0, [0, 1])

# Axes == [0, 1]
self._testClipIndexedSlicesByNorm(values, indices, shape, 4.0, [0, 2])

# Axes == [0, 1]
self._testClipIndexedSlicesByNorm(values, indices, shape, 4.0, [1, 2])

# Axes == [0, 1]
self._testClipIndexedSlicesByNorm(values, indices, shape, 4.0, [0, 1, 2])
