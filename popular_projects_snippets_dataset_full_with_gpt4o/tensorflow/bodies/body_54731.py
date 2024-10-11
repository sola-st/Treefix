# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
t = tensor_util.make_tensor_proto((b"a", b"ab", b"abc", b"abcd"))
self.assertProtoEquals("""
      dtype: DT_STRING
      tensor_shape { dim { size: 4 } }
      string_val: "a"
      string_val: "ab"
      string_val: "abc"
      string_val: "abcd"
      """, t)
a = tensor_util.MakeNdarray(t)
self.assertEqual(np.object_, a.dtype)
self.assertAllEqual(np.array((b"a", b"ab", b"abc", b"abcd")), a)
