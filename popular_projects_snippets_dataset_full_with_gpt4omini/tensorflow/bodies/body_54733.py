# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
t = tensor_util.make_tensor_proto((1 + 2j), dtype=dtypes.complex64)
self.assertProtoEquals("""
      dtype: DT_COMPLEX64
      tensor_shape {}
      scomplex_val: 1
      scomplex_val: 2
      """, t)
a = tensor_util.MakeNdarray(t)
self.assertEqual(np.complex64, a.dtype)
self.assertAllEqual(np.array(1 + 2j), a)
