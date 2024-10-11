# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
mcs = tensor_shape.TensorShape(x).most_specific_compatible_shape(
    tensor_shape.TensorShape(y))
mcs_dims = mcs.dims
if expected is None or mcs_dims is None:
    self.assertIs(expected, mcs_dims)
else:
    self.assertEqual(expected, mcs.as_list())
