# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
m = self._m_100_by_784.gpu()
self._benchmark_nested_defun_matmul(
    m, transpose_b=True, num_iters=self._num_iters_100_by_784)
