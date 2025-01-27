# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
m = self._m_2_by_2.cpu()
self._benchmark_nested_defun_matmul(
    m, transpose_b=False, num_iters=self._num_iters_2_by_2)
