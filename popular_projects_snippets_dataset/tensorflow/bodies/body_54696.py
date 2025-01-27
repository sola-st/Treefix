# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
value = 10.0
t = tensor_util.make_tensor_proto(value)
self.assertProtoEquals("""
      dtype: DT_FLOAT
      tensor_shape {}
      float_val: %.1f
      """ % value, t)
a = tensor_util.MakeNdarray(t)
self.assertEqual(np.float32, a.dtype)
self.assertAllClose(np.array(value, dtype=np.float32), a)
