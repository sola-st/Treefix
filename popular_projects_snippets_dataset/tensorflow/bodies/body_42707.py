# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
n = np.array([[1, 2], [3, 4]], order="F")
t = _create_tensor(n)
self.assertAllEqual([[1, 2], [3, 4]], t)
