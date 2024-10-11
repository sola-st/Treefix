# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
with backprop.GradientTape() as tape:
    m = self._m_2
    tape.watch(m)
    self._run(lambda: gen_array_ops.identity(m), 30000)
