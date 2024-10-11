# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
# Test with arrays
array_a = np.random.rand(3, 1)
array_b = np.random.rand(3, 1)
array_c = np.random.rand(4, 2)

self.assertShapeEqual(array_a, array_b)
with self.assertRaises(AssertionError):
    self.assertShapeEqual(array_a, array_c)

# Test with tensors
tensor_x = random_ops.random_uniform((5, 2, 1))
tensor_y = random_ops.random_uniform((5, 2, 1))
tensor_z = random_ops.random_uniform((2, 4))

self.assertShapeEqual(tensor_x, tensor_y)
with self.assertRaises(AssertionError):
    self.assertShapeEqual(tensor_x, tensor_z)
