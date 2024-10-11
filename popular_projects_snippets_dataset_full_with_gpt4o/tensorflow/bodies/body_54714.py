# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
t = tensor_util.make_tensor_proto([10, 20, 30, 40], shape=[2, 2])
if sys.byteorder == "big":
    self.assertProtoEquals(r"""
        dtype: DT_INT32
        tensor_shape { dim { size: 2 } dim { size: 2 } }
        tensor_content: "\000\000\000\n\000\000\000\024\000\000\000\036\000\000\000("
        """, t)
else:
    self.assertProtoEquals(r"""
        dtype: DT_INT32
        tensor_shape { dim { size: 2 } dim { size: 2 } }
        tensor_content: "\n\000\000\000\024\000\000\000\036\000\000\000(\000\000\000"
        """, t)
a = tensor_util.MakeNdarray(t)
self.assertEqual(np.int32, a.dtype)
self.assertAllClose(np.array([[10, 20], [30, 40]], dtype=np.int32), a)
