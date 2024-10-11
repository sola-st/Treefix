# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
t = tensor_util.make_tensor_proto(np.array([10, 20, 30], dtype=nptype))
if sys.byteorder == "big":
    # pylint: disable=line-too-long
    self.assertProtoEquals(
        r"""
        dtype: %s
        tensor_shape { dim { size: 3 } }
        tensor_content: "\000\000\000\000\000\000\000\n\000\000\000\000\000\000\000\024\000\000\000\000\000\000\000\036"
        """ % proto_dtype, t)
    # pylint: enable=line-too-long
else:
    # pylint: disable=line-too-long
    self.assertProtoEquals(
        r"""
        dtype: %s
        tensor_shape { dim { size: 3 } }
        tensor_content: "\n\000\000\000\000\000\000\000\024\000\000\000\000\000\000\000\036\000\000\000\000\000\000\000"
        """ % proto_dtype, t)
    # pylint: enable=line-too-long
a = tensor_util.MakeNdarray(t)
self.assertEqual(nptype, a.dtype)
self.assertAllClose(np.array([10, 20, 30], dtype=nptype), a)
