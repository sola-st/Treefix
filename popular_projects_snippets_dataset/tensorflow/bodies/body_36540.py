# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
# Compare the shapes, treating None dimensions as equal. We do not
# directly check actual_tensor_shape and tf.TensorShape(shape) for
# equality because tf.Dimension.__eq__ returns None if either dimension is
# None.
if shape is None:
    self.assertIsNone(actual_tensor_shape.dims)
else:
    self.assertListEqual(actual_tensor_shape.as_list(), shape)
