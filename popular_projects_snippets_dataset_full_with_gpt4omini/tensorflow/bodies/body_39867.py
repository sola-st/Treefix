# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
with context.device(device):
    a = array_ops.ones((2, 2))
    b = array_ops.ones((2, 2))
    func = lambda: math_ops.tensordot(a, b, [[1], [0]])
    self._run(func, 30000, execution_mode=execution_mode)
