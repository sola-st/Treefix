# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/data_structures_test.py
initial_list = constant_op.constant([[1, 2], [3, 4]])
elem_shape = constant_op.constant([2])
l = list_ops.tensor_list_from_tensor(initial_list, element_shape=elem_shape)

opts = data_structures.ListStackOpts(
    element_dtype=initial_list.dtype, original_call=None)

with self.cached_session() as sess:
    t = data_structures.list_stack(l, opts)
    self.assertAllEqual(self.evaluate(t), self.evaluate(initial_list))
