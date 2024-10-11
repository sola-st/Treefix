# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
if self.backend.platform not in {"cpu", "gpu"}:
    self.skipTest("Test requires cpu or gpu platform")
c = self._NewComputation()

def _Callback(x, y):
    assert y is None, y
    exit((None, x + 1))

arg0 = np.array([9, 43, -101, 22], dtype=np.int32)
shape = xla_client.shape_from_pyval(arg0)
token_shape = xla_client.Shape.token_shape()
p0 = ops.Parameter(c, 0, shape)
token = ops.CreateToken(c)
out, keepalive = self.backend.emit_python_callback(
    _Callback, c, [p0, token], [token_shape, shape])
out = ops.GetTupleElement(out, 1)
self._ExecuteAndCompareExact(c, arguments=[arg0], expected=[arg0 + 1])
del out, keepalive
