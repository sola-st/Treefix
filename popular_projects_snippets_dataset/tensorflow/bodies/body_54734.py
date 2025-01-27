# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
t = tensor_util.make_tensor_proto((1 + 2j), dtype=dtypes.complex128)
self.assertProtoEquals("""
      dtype: DT_COMPLEX128
      tensor_shape {}
      dcomplex_val: 1
      dcomplex_val: 2
      """, t)
a = tensor_util.MakeNdarray(t)
self.assertEqual(np.complex128, a.dtype)
self.assertAllEqual(np.array(1 + 2j), a)
