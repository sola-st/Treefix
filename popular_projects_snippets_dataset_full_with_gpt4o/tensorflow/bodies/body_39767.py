# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
if not context.num_gpus():
    exit()
with context.device(GPU):
    m1 = self._m_8_28_28_3.gpu()
    m2 = self._m_1_3_3_1.gpu()
    self._benchmark_tf_conv2d(m1, m2, 30000)
