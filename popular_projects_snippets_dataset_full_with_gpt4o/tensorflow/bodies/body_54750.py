# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
x = indexed_slices.IndexedSlices(
    constant_op.constant([1, 2, 3]), constant_op.constant([10, 20, 30]))
x_value = indexed_slices.IndexedSlicesValue(
    np.array([1, 2, 3]), np.array([10, 20, 30]), np.array([100]))
self.assertTrue(tensor_util.is_tf_type(x))
self.assertFalse(tensor_util.is_tf_type(x_value))
