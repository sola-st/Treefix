# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
t = tensor_util.make_tensor_proto("foo")
self.assertProtoEquals("""
      dtype: DT_STRING
      tensor_shape {}
      string_val: "foo"
      """, t)
a = tensor_util.MakeNdarray(t)
self.assertEqual(np.object_, a.dtype)
self.assertEqual([b"foo"], a)
