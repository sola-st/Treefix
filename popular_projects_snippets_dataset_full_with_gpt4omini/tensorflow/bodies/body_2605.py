# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
samples = [
    NumpyArrayF32(42.0),
    NumpyArrayF32([97.0]),
    NumpyArrayF32([64.0, 117.0]),
    NumpyArrayF32([[2.0, 3.0], [4.0, 5.0]]),
]
for lhs in samples:
    c = self._NewComputation()
    ops.CrossReplicaSum(ops.Constant(c, lhs))
    self._ExecuteAndCompareExact(c, expected=[lhs])
