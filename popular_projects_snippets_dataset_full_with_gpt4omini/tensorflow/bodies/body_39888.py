# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
with context.device(device):
    func = lambda: array_ops.zeros_like(m)
    self._run(func, 3000)
