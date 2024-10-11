# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/slices_test.py
initial_list = constant_op.constant([[1, 2], [3, 4]])
elem_shape = constant_op.constant([2])
l = list_ops.tensor_list_from_tensor(initial_list, element_shape=elem_shape)
l = slices.set_item(l, 0, [5, 6])

with self.cached_session() as sess:
    t = list_ops.tensor_list_stack(l, element_dtype=initial_list.dtype)
    self.assertAllEqual(self.evaluate(t), [[5, 6], [3, 4]])
