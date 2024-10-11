# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
if not context.num_gpus():
    exit()
with context.device(GPU):
    m = self._m_2.gpu()
    self._benchmark_tf_multiply_op(m, 30000)
