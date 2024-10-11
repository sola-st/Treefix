# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
array = np.array([[1], [2]])
correct_shape = (2, 1)
incorrect_shape = (1, 2)
tensor_util.make_tensor_proto(array, shape=correct_shape, verify_shape=True)
with self.assertRaises(TypeError):
    tensor_util.make_tensor_proto(
        array, shape=incorrect_shape, verify_shape=True)
