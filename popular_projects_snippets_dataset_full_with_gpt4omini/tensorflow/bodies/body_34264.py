# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
c = constant_op.constant([1, 2], dtype=dtypes.int64)
l = list_ops.tensor_list_from_tensor(c, element_shape=[])
v = vs.get_variable("var", initializer=[l] * 10, use_resource=True)
v_r_0_stacked = list_ops.tensor_list_stack(v[0], dtypes.int64)
self.evaluate(v.initializer)
self.assertAllEqual([1, 2], self.evaluate(v_r_0_stacked))
v_r_sparse_stacked = list_ops.tensor_list_stack(
    v.sparse_read(0), dtypes.int64)
self.assertAllEqual([1, 2], self.evaluate(v_r_sparse_stacked))
c34 = constant_op.constant([3, 4], dtype=dtypes.int64)
l_new_0 = list_ops.tensor_list_from_tensor(c34, element_shape=[])
c56 = constant_op.constant([5, 6], dtype=dtypes.int64)
l_new_1 = list_ops.tensor_list_from_tensor(c56, element_shape=[])
updated_v = state_ops.scatter_update(v, [3, 5], [l_new_0, l_new_1])
updated_v_elems = array_ops.unstack(updated_v)
updated_v_stacked = [
    list_ops.tensor_list_stack(el, dtypes.int64) for el in updated_v_elems
]
expected = ([[1, 2]] * 3 + [[3, 4], [1, 2], [5, 6]] +
            [[1, 2]] * 4)
self.assertAllEqual(self.evaluate(updated_v_stacked), expected)
