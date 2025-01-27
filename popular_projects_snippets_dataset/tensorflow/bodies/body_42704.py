# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
values = np.array([3.0])
t = _create_tensor(values)
self.assertAllEqual(values, t)
