# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
# Test with array.
t = tensor_util.make_tensor_proto([10, 20, 30], dtype=dtype)
self.assertEqual(dtype, t.dtype)
self.assertProtoEquals("dim { size: 3 }", t.tensor_shape)
a = tensor_util.MakeNdarray(t)
self.assertEqual(nptype, a.dtype)
self.assertAllClose(np.array([10, 20, 30], dtype=nptype), a)
# Test with ndarray.
t = tensor_util.make_tensor_proto(np.array([10, 20, 30], dtype=nptype))
self.assertEqual(dtype, t.dtype)
self.assertProtoEquals("dim { size: 3 }", t.tensor_shape)
a = tensor_util.MakeNdarray(t)
self.assertEqual(nptype, a.dtype)
self.assertAllClose(np.array([10, 20, 30], dtype=nptype), a)
