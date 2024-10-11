# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
st = sparse_tensor.SparseTensor([[1, 2]], [3], [10, 10])
st_value = self.evaluate(st)
self.assertTrue(tensor_util.is_tf_type(st))
self.assertFalse(tensor_util.is_tf_type(st_value))
