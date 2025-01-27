# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util_test.py
# Tests set_tensor_shape where the tensor name passed in doesn't exist.
with ops.Graph().as_default():
    tensor = array_ops.placeholder(dtype=dtypes.float32, shape=[None, 3, 5])
self.assertAllEqual([None, 3, 5], tensor.shape)

with self.assertRaises(ValueError) as error:
    util.set_tensor_shapes([tensor], {"invalid-input": [5, 3, 5]})
self.assertEqual(
    "Invalid tensor 'invalid-input' found in tensor shapes map.",
    str(error.exception))
self.assertAllEqual([None, 3, 5], tensor.shape)
