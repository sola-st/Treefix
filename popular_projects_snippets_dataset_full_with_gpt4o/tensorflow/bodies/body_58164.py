# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util_test.py
# Tests set_tensor_shape where the shape passed in is incompatible.
with ops.Graph().as_default():
    tensor = array_ops.placeholder(dtype=dtypes.float32, shape=[None, 3, 5])
self.assertAllEqual([None, 3, 5], tensor.shape)

with self.assertRaises(ValueError) as error:
    util.set_tensor_shapes([tensor], {"Placeholder": [1, 5, 5]})
self.assertIn("The shape of tensor 'Placeholder' cannot be changed",
              str(error.exception))
self.assertAllEqual([None, 3, 5], tensor.shape)
