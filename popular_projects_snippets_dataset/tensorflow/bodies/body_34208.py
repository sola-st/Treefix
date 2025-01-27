# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.tensor_list_reserve(
    element_dtype=dtypes.float32, element_shape=[], num_elements=3)
t = list_ops.tensor_list_gather(l, [0, 2], element_dtype=dtypes.float32)
self.assertAllEqual(self.evaluate(t), [0., 0.])
