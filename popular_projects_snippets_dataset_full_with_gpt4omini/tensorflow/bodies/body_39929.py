# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
if not context.num_gpus():
    exit()
with context.device(GPU):
    m = resource_variable_ops.ResourceVariable(self._m_2_by_2.gpu())
    self._benchmark_read_variable(m, num_iters=self._num_iters_2_by_2)
