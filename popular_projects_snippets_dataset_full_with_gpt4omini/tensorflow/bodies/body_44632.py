# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/slices_test.py
initial_list = constant_op.constant([[1, 2], [3, 4]])
elem_shape = constant_op.constant([2])
l = list_ops.tensor_list_from_tensor(initial_list, element_shape=elem_shape)
t = slices.get_item(
    l, 1, slices.GetItemOpts(element_dtype=initial_list.dtype))

with self.cached_session() as sess:
    self.assertAllEqual(self.evaluate(t), [3, 4])
