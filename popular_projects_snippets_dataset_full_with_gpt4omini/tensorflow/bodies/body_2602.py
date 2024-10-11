# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
if ((src_dtype in [np.int64, np.float64] or
     dst_dtype in [np.int64, np.float64]) and
    self.backend.platform == "tpu"):
    self.skipTest("TPU doesn't support float64")
c = self._NewComputation()
x = np.array([0, 1, 0, 0, 1], dtype=src_dtype)
ops.ConvertElementType(
    ops.Constant(c, x), xla_client.dtype_to_etype(dst_dtype))

result = xla_client.execute_with_python_values(
    self.backend.compile(c.build()), (), backend=self.backend)
self.assertLen(result, 1)
expected = np.array(x, dtype=dst_dtype)

self.assertEqual(result[0].shape, expected.shape)
self.assertEqual(result[0].dtype, expected.dtype)
np.testing.assert_equal(result[0], expected)
