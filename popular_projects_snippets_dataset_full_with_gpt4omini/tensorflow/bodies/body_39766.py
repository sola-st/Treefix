# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
with context.device(CPU):
    m1 = self._m_8_28_28_3.cpu()
    m2 = self._m_1_3_3_1.cpu()
    self._benchmark_tf_conv2d(m1, m2, 30000)
