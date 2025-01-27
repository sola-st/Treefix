# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
if self.backend.platform not in {"cpu", "gpu"}:
    self.skipTest("Test requires cpu or gpu platform")
c = self._NewComputation()

f = lambda x, y: (x + y, x - y)

arg0 = np.array([9, 43, -101, 22], dtype=np.int32)
arg1 = np.array([10, 15, -2, 7], dtype=np.int32)
shape = xla_client.shape_from_pyval(arg0)
shape = shape.with_major_to_minor_layout_if_absent()
p0 = ops.Parameter(c, 0, shape)
p1 = ops.Parameter(c, 1, shape)
out, keepalive = self.backend.emit_python_callback(
    f, c, [p0, p1], [shape, shape])
self._ExecuteAndCompareExact(
    c, arguments=[arg0, arg1], expected=[arg0 + arg1, arg0 - arg1])
del out, keepalive
