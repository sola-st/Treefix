# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
if self.backend.platform not in {"cpu", "gpu"}:
    self.skipTest("Test requires cpu or gpu platform")
c = self._NewComputation()

def _Callback(x):
    raise ValueError("Value error raised!")

arg0 = np.array([9, 43, -101, 22], dtype=np.int32)
shape = xla_client.shape_from_pyval(arg0)
shape = shape.with_major_to_minor_layout_if_absent()
p0 = ops.Parameter(c, 0, shape)
out, keepalive = self.backend.emit_python_callback(
    _Callback, c, [p0], [shape], has_side_effects=True)
with self.assertRaisesRegex(xla_client.XlaRuntimeError,
                            "Value error raised!"):
    self._Execute(c, [arg0])
del out, keepalive
