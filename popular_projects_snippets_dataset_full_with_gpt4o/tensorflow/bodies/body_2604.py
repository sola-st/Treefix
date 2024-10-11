# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
samples = [
    NumpyArrayF32([97.0]),
    NumpyArrayF32([64.0, 117.0]),
    NumpyArrayF32([[2.0, 3.0], [4.0, 5.0]]),
]
for lhs in samples[:1]:
    c = self._NewComputation()
    ops.AllToAll(ops.Constant(c, lhs), 0, 0)
    self._ExecuteAndCompareExact(c, expected=[lhs])
