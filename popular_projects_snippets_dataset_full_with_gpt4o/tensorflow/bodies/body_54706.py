# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
t = tensor_util.make_tensor_proto([10.0, 20.0, 30.0], dtype=dtypes.float32)
a = tensor_util.MakeNdarray(t)
a[0] = 5.0
self.assertEqual(np.float32, a.dtype)
self.assertAllClose(np.array([5.0, 20.0, 30.0], dtype=np.float32), a)
if sys.byteorder == "big":
    self.assertProtoEquals(r"""
        dtype: DT_FLOAT
        tensor_shape { dim { size: 3 } }
        tensor_content: "A \000\000A\240\000\000A\360\000\000"
        """, t)
else:
    self.assertProtoEquals(r"""
        dtype: DT_FLOAT
        tensor_shape { dim { size: 3 } }
        tensor_content: "\000\000 A\000\000\240A\000\000\360A"
        """, t)
