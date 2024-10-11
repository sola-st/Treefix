# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py

# Test mixed multi-dimensional inputs
array_input = np.random.rand(4, 3, 2)
tensor_input = random_ops.random_uniform((4, 3, 2))
tensor_input_2 = random_ops.random_uniform((10, 5))

self.assertShapeEqual(array_input, tensor_input)
self.assertShapeEqual(tensor_input, array_input)
with self.assertRaises(AssertionError):
    self.assertShapeEqual(array_input, tensor_input_2)

# Test with scalar inputs
array_input = np.random.rand(1)
tensor_input = random_ops.random_uniform((1,))
tensor_input_2 = random_ops.random_uniform((3, 1))

self.assertShapeEqual(array_input, tensor_input)
self.assertShapeEqual(tensor_input, array_input)
with self.assertRaises(AssertionError):
    self.assertShapeEqual(array_input, tensor_input_2)
