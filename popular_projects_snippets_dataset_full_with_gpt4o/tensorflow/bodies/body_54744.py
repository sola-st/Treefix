# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
with self.assertRaises(ValueError):
    tensor_util.make_tensor_proto(np.array([1, 2]), shape=[1])
