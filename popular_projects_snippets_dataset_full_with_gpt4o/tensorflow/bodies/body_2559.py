# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
shape = xla_client.Shape.array_shape(
    xla_client.dtype_to_etype(dtype), (2, 3))
ops.Iota(c, shape, 1)
expected = np.array([[0, 1, 2], [0, 1, 2]], dtype=dtype)
self._ExecuteAndCompareExact(c, expected=[expected])
