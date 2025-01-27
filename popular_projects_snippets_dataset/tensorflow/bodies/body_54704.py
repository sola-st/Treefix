# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
t = tensor_util.make_tensor_proto(
    np.array([[10.0, 20.0, 30.0]], dtype=np.float64))
if sys.byteorder == "big":
    self.assertProtoEquals(r"""
        dtype: DT_DOUBLE
        tensor_shape { dim { size: 1 } dim { size: 3 } }
        tensor_content: "@$\000\000\000\000\000\000@4\000\000\000\000\000\000@>\000\000\000\000\000\000"
        """, t)
else:
    self.assertProtoEquals(r"""
        dtype: DT_DOUBLE
        tensor_shape { dim { size: 1 } dim { size: 3 } }
        tensor_content: "\000\000\000\000\000\000$@\000\000\000\000\000\0004@\000\000\000\000\000\000>@"
        """, t)
a = tensor_util.MakeNdarray(t)
self.assertEqual(np.float64, a.dtype)
self.assertAllClose(
    np.array([[10.0, 20.0, 30.0]], dtype=np.float64),
    tensor_util.MakeNdarray(t))
