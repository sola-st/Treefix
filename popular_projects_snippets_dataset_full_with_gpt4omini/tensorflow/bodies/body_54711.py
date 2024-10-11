# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
t = tensor_util.make_tensor_proto(10)
self.assertProtoEquals("""
      dtype: DT_INT32
      tensor_shape {}
      int_val: 10
      """, t)
a = tensor_util.MakeNdarray(t)
self.assertEqual(np.int32, a.dtype)
self.assertAllClose(np.array(10, dtype=np.int32), a)
