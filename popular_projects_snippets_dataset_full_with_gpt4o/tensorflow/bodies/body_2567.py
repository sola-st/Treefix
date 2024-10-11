# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
# sum of a 2D array with a 1D array where the latter is replicated across
# dimension 0 to match the former's shape.
c = self._NewComputation()
ops.Add(
    ops.Constant(c,
                 np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                          dtype=dtype)),
    ops.Constant(c, np.array([10, 20, 30], dtype=dtype)),
    broadcast_dimensions=(0,))
self._ExecuteAndCompareClose(
    c, expected=[[[11, 12, 13], [24, 25, 26], [37, 38, 39]]])
