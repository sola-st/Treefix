# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
t = tensor_util.make_tensor_proto(np.array([10.0, 20.0], dtype=np.float16))
self.assertProtoEquals(
    """
      dtype: DT_HALF
      tensor_shape { dim { size: 2 } }
      tensor_content: "\000I\000M"
      """, t)

a = tensor_util.MakeNdarray(t)
self.assertEqual(np.float16, a.dtype)
self.assertAllClose(np.array([10.0, 20.0], dtype=np.float16), a)
