# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
# Github issue: 11974
dtype = dtypes.int32
nptype = np.int32
t = tensor_util.make_tensor_proto(
    [10, tensor_shape.Dimension(20), 30], dtype=dtype)
self.assertEqual(dtype, t.dtype)
a = tensor_util.MakeNdarray(t)
self.assertEqual(nptype, a.dtype)
self.assertAllClose(np.array([10, 20, 30], dtype=nptype), a)
