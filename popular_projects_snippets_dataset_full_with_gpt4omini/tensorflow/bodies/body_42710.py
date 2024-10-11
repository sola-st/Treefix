# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
numpy_tensor = np.asarray(1.0)
tensor = constant_op.constant(numpy_tensor)
with self.assertRaises(TypeError):
    len(numpy_tensor)
with self.assertRaisesRegex(TypeError, r"Scalar tensor has no `len[(][)]`"):
    len(tensor)

numpy_tensor = np.asarray([1.0, 2.0, 3.0])
tensor = constant_op.constant(numpy_tensor)
self.assertAllEqual(len(numpy_tensor), len(tensor))

numpy_tensor = np.asarray([[1.0, 2.0, 3.0], [1.0, 2.0, 3.0]])
tensor = constant_op.constant(numpy_tensor)
self.assertAllEqual(len(numpy_tensor), len(tensor))
