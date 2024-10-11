# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.Add(
    ops.Parameter(c, 0, xla_client.shape_from_pyval(NumpyArrayF32(0.))),
    ops.Constant(c, np.float32(3.14)))
arg = NumpyArrayF32(1.11)
compiled_c = self.backend.compile(c.build())
arg_buffer = self.backend.buffer_from_pyval(arg)
arg_buffer.delete()
with self.assertRaises(xla_client.XlaRuntimeError):
    compiled_c.execute([arg_buffer])
