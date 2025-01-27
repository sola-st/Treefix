# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
with backprop.GradientTape() as tape:
    tape.watch(m)
    self._run(m.value, num_iters)
