# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
with context.device(device):
    func = lambda: array_ops.zeros(shape, dtype)
    self._run(func, 3000)
