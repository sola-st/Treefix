# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
with context.device(CPU):
    m = gen_array_ops.identity(self._m_2)
    self._run(lambda: backprop.gradients_function(lambda x: x, [0])(m), 30000)
