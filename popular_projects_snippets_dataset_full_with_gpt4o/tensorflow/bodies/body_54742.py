# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
with self.assertRaises(TypeError):
    tensor_util.make_tensor_proto(np.array([1]), 0)
with self.assertRaises(TypeError):
    tensor_util.make_tensor_proto(3, dtype=dtypes.qint8)
with self.assertRaises(TypeError):
    tensor_util.make_tensor_proto([3], dtype=dtypes.qint8)

# Validate the helpful error message when trying to convert an
# unconvertible list as strings.
with self.assertRaisesRegex(TypeError, "Failed to convert elements"):
    tensor_util.make_tensor_proto([tensor_shape.Dimension(1)])
