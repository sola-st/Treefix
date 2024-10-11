# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.tensor_list_reserve(
    element_dtype=dtypes.float32, element_shape=None, num_elements=3)
t = gen_list_ops.tensor_list_gather(
    l, [0, 1, 2], element_dtype=dtypes.float32, element_shape=[])
self.assertEqual(t.shape.as_list(), [3])
self.assertAllEqual(self.evaluate(t), np.zeros((3,)))
