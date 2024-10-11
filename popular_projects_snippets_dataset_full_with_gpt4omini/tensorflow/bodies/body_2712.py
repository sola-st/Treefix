# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
c.set_op_metadata(xla_client.CurrentSourceInfoMetadata())
ops.Parameter(c, 0, xla_client.shape_from_pyval(self.s32_scalar_2))
c.clear_op_metadata()

def TestFun():
    exit(xla_client.execute_with_python_values(
        self.backend.compile(c.build()), [self.f32_scalar_2], self.backend))

self.assertRaisesRegex(
    RuntimeError, r"Invalid argument: Argument does not match.*"
    r"want s32\[\], got f32\[\].*", TestFun)
