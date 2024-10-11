# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
value = np.iinfo(np.int64).max
t = tensor_util.make_tensor_proto(value)
self.assertProtoEquals("""
      dtype: DT_INT64
      tensor_shape {}
      int64_val: %d
      """ % value, t)
a = tensor_util.MakeNdarray(t)
self.assertEqual(np.int64, a.dtype)
self.assertAllClose(np.array(value, dtype=np.int64), a)
