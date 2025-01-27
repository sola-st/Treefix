# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
t = tensor_util.make_tensor_proto(
    [(1 + 2j), (3 + 4j), (5 + 6j)], shape=[1, 3], dtype=dtypes.complex64)
self.assertProtoEquals("""
      dtype: DT_COMPLEX64
      tensor_shape { dim { size: 1 } dim { size: 3 } }
      scomplex_val: 1
      scomplex_val: 2
      scomplex_val: 3
      scomplex_val: 4
      scomplex_val: 5
      scomplex_val: 6
      """, t)
a = tensor_util.MakeNdarray(t)
self.assertEqual(np.complex64, a.dtype)
self.assertAllEqual(np.array([[(1 + 2j), (3 + 4j), (5 + 6j)]]), a)
