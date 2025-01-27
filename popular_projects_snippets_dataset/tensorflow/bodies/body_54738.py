# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
t = tensor_util.make_tensor_proto(
    np.array([[(1 + 2j), (3 + 4j)], [(5 + 6j), (7 + 8j)]]),
    dtype=dtypes.complex64)
# scomplex_val are real_0, imag_0, real_1, imag_1, ...
self.assertProtoEquals("""
      dtype: DT_COMPLEX64
      tensor_shape { dim { size: 2 } dim { size: 2 } }
      scomplex_val: 1
      scomplex_val: 2
      scomplex_val: 3
      scomplex_val: 4
      scomplex_val: 5
      scomplex_val: 6
      scomplex_val: 7
      scomplex_val: 8
      """, t)
a = tensor_util.MakeNdarray(t)
self.assertEqual(np.complex64, a.dtype)
self.assertAllEqual(
    np.array([[(1 + 2j), (3 + 4j)], [(5 + 6j), (7 + 8j)]]), a)
