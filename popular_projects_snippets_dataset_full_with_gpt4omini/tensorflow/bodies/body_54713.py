# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
# We don't use the min np.int64 value here
# because it breaks np.abs().
#
# np.iinfo(np.int64).min = -9223372036854775808
# np.iinfo(np.int64).max = 9223372036854775807
# np.abs(-9223372036854775808) = -9223372036854775808
value = np.iinfo(np.int64).min + 1
t = tensor_util.make_tensor_proto(value)
self.assertProtoEquals("""
      dtype: DT_INT64
      tensor_shape {}
      int64_val: %d
      """ % value, t)
a = tensor_util.MakeNdarray(t)
self.assertEqual(np.int64, a.dtype)
self.assertAllClose(np.array(value, dtype=np.int64), a)
