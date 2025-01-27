# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
numpy_tensor = np.asarray(1.0)
tensor = constant_op.constant(numpy_tensor)
self.assertAllEqual(numpy_tensor.ndim, tensor.ndim)

numpy_tensor = np.asarray([1.0, 2.0, 3.0])
tensor = constant_op.constant(numpy_tensor)
self.assertAllEqual(numpy_tensor.ndim, tensor.ndim)

numpy_tensor = np.asarray([[1.0, 2.0, 3.0], [1.0, 2.0, 3.0]])
tensor = constant_op.constant(numpy_tensor)
self.assertAllEqual(numpy_tensor.ndim, tensor.ndim)
