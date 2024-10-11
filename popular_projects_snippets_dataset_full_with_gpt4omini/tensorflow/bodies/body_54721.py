# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
# Test with array.
data = [(21,), (22,), (23,)]

t = tensor_util.make_tensor_proto(data, dtype=dtypes.qint32)
if sys.byteorder == "big":
    self.assertProtoEquals(r"""
        dtype: DT_QINT32
        tensor_shape { dim { size: 3 } }
        tensor_content: "\000\000\000\025\000\000\000\026\000\000\000\027"
        """, t)
else:
    self.assertProtoEquals(r"""
        dtype: DT_QINT32
        tensor_shape { dim { size: 3 } }
        tensor_content: "\025\000\000\000\026\000\000\000\027\000\000\000"
        """, t)
a = tensor_util.MakeNdarray(t)
self.assertEqual(dtypes.qint32.as_numpy_dtype, a.dtype)
self.assertAllEqual(np.array(data, dtype=a.dtype), a)

t = tensor_util.make_tensor_proto(data, dtype=dtypes.quint8)
self.assertProtoEquals(r"""
      dtype: DT_QUINT8
      tensor_shape { dim { size: 3 } }
      tensor_content: "\025\026\027"
      """, t)
a = tensor_util.MakeNdarray(t)
self.assertEqual(dtypes.quint8.as_numpy_dtype, a.dtype)
self.assertAllEqual(np.array(data, dtype=a.dtype), a)

t = tensor_util.make_tensor_proto(data, dtype=dtypes.qint8)
self.assertProtoEquals(r"""
      dtype: DT_QINT8
      tensor_shape { dim { size: 3 } }
      tensor_content: "\025\026\027"
      """, t)
a = tensor_util.MakeNdarray(t)
self.assertEqual(dtypes.qint8.as_numpy_dtype, a.dtype)
self.assertAllEqual(np.array(data, dtype=a.dtype), a)

t = tensor_util.make_tensor_proto(data, dtype=dtypes.quint16)
if sys.byteorder == "big":
    self.assertProtoEquals(r"""
        dtype: DT_QUINT16
        tensor_shape { dim { size: 3 } }
        tensor_content: "\000\025\000\026\000\027"
        """, t)
else:
    self.assertProtoEquals(r"""
        dtype: DT_QUINT16
        tensor_shape { dim { size: 3 } }
        tensor_content: "\025\000\026\000\027\000"
        """, t)
a = tensor_util.MakeNdarray(t)
self.assertEqual(dtypes.quint16.as_numpy_dtype, a.dtype)
self.assertAllEqual(np.array(data, dtype=a.dtype), a)

t = tensor_util.make_tensor_proto(data, dtype=dtypes.qint16)
if sys.byteorder == "big":
    self.assertProtoEquals(r"""
        dtype: DT_QINT16
        tensor_shape { dim { size: 3 } }
        tensor_content: "\000\025\000\026\000\027"
        """, t)
else:
    self.assertProtoEquals(r"""
        dtype: DT_QINT16
        tensor_shape { dim { size: 3 } }
        tensor_content: "\025\000\026\000\027\000"
        """, t)
a = tensor_util.MakeNdarray(t)
self.assertEqual(dtypes.qint16.as_numpy_dtype, a.dtype)
self.assertAllEqual(np.array(data, dtype=a.dtype), a)
