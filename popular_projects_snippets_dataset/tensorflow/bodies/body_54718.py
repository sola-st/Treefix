# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
t = tensor_util.make_tensor_proto(10, dtype=dtype)
self.assertProtoEquals(
    """
      dtype: %s
      tensor_shape {}
      %s: 10
    """ % (proto_dtype, proto_value_name), t)
a = tensor_util.MakeNdarray(t)
self.assertEqual(nptype, a.dtype)
self.assertAllClose(np.array(10, dtype=nptype), a)
