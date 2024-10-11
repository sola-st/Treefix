# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
with context.device(CPU):
    m = resource_variable_ops.ResourceVariable(self._m_2_by_2)
    self._benchmark_read_variable_with_tape(
        m, num_iters=self._num_iters_2_by_2)
