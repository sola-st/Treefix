# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
if self.backend.platform not in {"cpu", "gpu"}:
    self.skipTest("Test requires cpu or gpu platform")
c = self._NewComputation()

def _Callback(x):
    assert x.flags.f_contiguous, x.strides
    # Force the output array to have C layout, which will require a
    # transpose back to the expected Fortran layout.
    exit((np.ascontiguousarray(x * 2),))

arg0 = np.arange(12, dtype=np.int16).reshape(3, 4)
shape_f_layout = xla_client.Shape.array_shape(
    arg0.dtype, arg0.shape, layout=(0, 1))
p0 = ops.Parameter(c, 0, xla_client.shape_from_pyval(arg0))
out, keepalive = self.backend.emit_python_callback(
    _Callback, c, [p0], [shape_f_layout], [shape_f_layout])
self._ExecuteAndCompareExact(c, arguments=[arg0], expected=[arg0 * 2])
del out, keepalive
