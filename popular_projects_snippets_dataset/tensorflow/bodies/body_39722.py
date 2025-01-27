# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
# used for multiply benchmarks
self._m_2 = random_ops.random_uniform([2])

# used for matmul benchmarks
self._m_2_by_2 = random_ops.random_uniform((2, 2))
self._m_100_by_784 = random_ops.random_uniform((100, 784))

self._num_iters_2_by_2 = 30000
self._num_iters_100_by_784 = 30000

# used for conv2d benchmarks
self._m_8_28_28_3 = random_ops.random_uniform((8, 28, 28, 3))
self._m_1_3_3_1 = random_ops.random_uniform((1, 3, 3, 1))
