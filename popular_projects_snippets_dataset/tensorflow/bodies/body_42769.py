# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
a = [[1., 1], [1j, 2j]]
np_value = np.array(a, dtype=np.complex128)
tf_value = ops.convert_to_tensor(a, dtype=dtypes.complex128)
self.assertAllEqual(tf_value.numpy(), np_value)
