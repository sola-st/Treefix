# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/data_structures_test.py
initial_list = constant_op.constant([[1, 2], [3, 4]])
elem_shape = constant_op.constant([2])
l = list_ops.tensor_list_from_tensor(initial_list, element_shape=elem_shape)

opts = data_structures.ListPopOpts(
    element_dtype=initial_list.dtype,
    element_shape=(2,))

with self.assertRaises(NotImplementedError):
    data_structures.list_pop(l, 0, opts)

with self.cached_session() as sess:
    l, x = data_structures.list_pop(l, None, opts)
    self.assertAllEqual(self.evaluate(x), [3, 4])

    t = list_ops.tensor_list_stack(l, element_dtype=initial_list.dtype)
    self.assertAllEqual(self.evaluate(t), [[1, 2]])
