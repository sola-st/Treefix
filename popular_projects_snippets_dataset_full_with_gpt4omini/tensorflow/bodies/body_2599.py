# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
x = np.array([[3., 4., 5.]], np.float32)
y = self.backend.buffer_from_pyval(x)
z = y.clone()
self.assertNotEqual(id(x), id(y))
np.testing.assert_array_equal(np.asarray(y), np.asarray(z))
self.assertEqual(y.unsafe_buffer_pointer(), z.unsafe_buffer_pointer())
