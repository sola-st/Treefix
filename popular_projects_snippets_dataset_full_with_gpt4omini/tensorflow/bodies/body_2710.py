# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
c.set_op_metadata(xla_client.CurrentSourceInfoMetadata())
ops.Parameter(c, 0, xla_client.shape_from_pyval(self.s32_scalar_2))
c.clear_op_metadata()

options = xla_client.CompileOptions()
options.argument_layouts = [
    xla_client.Shape.array_shape(np.dtype(np.float32), [])
]

def TestFun():
    exit(self.backend.compile(c.build(), compile_options=options))

self.assertRaisesRegex(
    RuntimeError, r".*Invalid argument shape.*"
    r"expected s32\[\], got f32\[\].*", TestFun)
