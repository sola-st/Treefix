# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
with context.device(GPU):
    m = self._m_2_by_2.gpu()
    self._benchmark_transpose(m, num_iters=self._num_iters_2_by_2)
