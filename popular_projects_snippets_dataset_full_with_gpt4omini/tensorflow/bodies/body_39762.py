# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
with context.device(CPU):
    m = self._m_2.cpu()
    self._benchmark_tf_multiply(m, 30000)
