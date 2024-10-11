# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l0 = list_ops.tensor_list_reserve([], 3, element_dtype=dtypes.float32)
l1 = list_ops.tensor_list_set_item(l0, 0, 1.)  # [1., _, _]
zeros_1 = array_ops.zeros_like(l1)  # [0., _, _]
l2 = list_ops.tensor_list_set_item(l1, 2, 2.)  # [1., _, 2.]
zeros_2 = array_ops.zeros_like(l2)  # [0., _, 0.]

# Gather indices with zeros in `zeros_1`.
res_1 = list_ops.tensor_list_gather(
    zeros_1, [0], element_dtype=dtypes.float32)
# Gather indices with zeros in `zeros_2`.
res_2 = list_ops.tensor_list_gather(
    zeros_2, [0, 2], element_dtype=dtypes.float32)

self.assertAllEqual(self.evaluate(res_1), [0.])
self.assertAllEqual(self.evaluate(res_2), [0., 0.])
