# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
if (np.float64 in (src_dtype, dst_dtype) and
    self.backend.platform == "tpu"):
    self.skipTest("TPU doesn't support float64")
c = self._NewComputation()
x = np.array([0, 1, 0, 0, 1], dtype=src_dtype)
ops.BitcastConvertType(
    ops.Constant(c, x), xla_client.dtype_to_etype(dst_dtype))

result = xla_client.execute_with_python_values(
    self.backend.compile(c.build()), (), backend=self.backend)
self.assertLen(result, 1)
expected = x.view(dst_dtype)

self.assertEqual(result[0].shape, expected.shape)
self.assertEqual(result[0].dtype, expected.dtype)
np.testing.assert_equal(result[0], expected)
