# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
with context.device(CPU):
    m = self._m_2_by_2.cpu()
    self._benchmark_transpose(m, num_iters=self._num_iters_2_by_2)
