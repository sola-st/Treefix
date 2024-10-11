# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
arr = np.asarray([10, 20, 30], dtype="int")
t = tensor_util.make_tensor_proto(arr, dtype=dtypes.float32)
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
a = tensor_util.MakeNdarray(t)
self.assertEqual(np.float32, a.dtype)
self.assertAllClose(np.array([10.0, 20.0, 30.0], dtype=np.float32), a)
