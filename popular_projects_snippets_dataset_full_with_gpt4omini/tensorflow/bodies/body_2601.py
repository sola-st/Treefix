# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
args = (
    ops.Constant(c, np.array([1.0, 2.0, 3.0], dtype=dtype)),
    ops.Constant(c, np.array([4.0, 5.0, 6.0], dtype=dtype)),
)
ops.ConcatInDim(c, args, dimension=0)
self._ExecuteAndCompareExact(
    c, expected=[np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=dtype)])
