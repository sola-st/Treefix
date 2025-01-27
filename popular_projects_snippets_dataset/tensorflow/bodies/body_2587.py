# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
pyval = np.array([[1., 2.]], np.float32)
local_buffer = self.backend.buffer_from_pyval(pyval)
xla_shape = local_buffer.xla_shape()
self.assertEqual(xla_shape.dimensions(), (1, 2))
self.assertEqual(np.dtype(xla_shape.element_type()), np.dtype(np.float32))
