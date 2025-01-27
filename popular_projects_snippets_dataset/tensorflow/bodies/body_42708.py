# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
tensor = constant_op.constant([1.0, 2.0, 3.0])
numpy_tensor = np.asarray(tensor, dtype=np.int32)
self.assertAllEqual(numpy_tensor, [1, 2, 3])
