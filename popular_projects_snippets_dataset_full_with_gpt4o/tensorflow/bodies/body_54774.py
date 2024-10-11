# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
np_val = np.random.rand(3, 4, 7).astype(np.float32)
self.assertIs(np_val, tensor_util.constant_value(np_val))
