# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
t = tensor_util.make_tensor_proto(
    np.array([[(1 + 2j), (3 + 4j)], [(5 + 6j), (7 + 8j)]]),
    dtype=dtypes.complex128)
# scomplex_val are real_0, imag_0, real_1, imag_1, ...
self.assertProtoEquals("""
      dtype: DT_COMPLEX128
      tensor_shape { dim { size: 2 } dim { size: 2 } }
      dcomplex_val: 1
      dcomplex_val: 2
      dcomplex_val: 3
      dcomplex_val: 4
      dcomplex_val: 5
      dcomplex_val: 6
      dcomplex_val: 7
      dcomplex_val: 8
      """, t)
a = tensor_util.MakeNdarray(t)
self.assertEqual(np.complex128, a.dtype)
self.assertAllEqual(
    np.array([[(1 + 2j), (3 + 4j)], [(5 + 6j), (7 + 8j)]]), a)
