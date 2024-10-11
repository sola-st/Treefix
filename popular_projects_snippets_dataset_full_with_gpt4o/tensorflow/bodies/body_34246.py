# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
t = constant_op.constant([1.0, 2.0])
child_l = list_ops.tensor_list_from_tensor(t, element_shape=[])
l = list_ops.empty_tensor_list(
    element_shape=constant_op.constant([], dtype=dtypes.int32),
    element_dtype=dtypes.variant)
l = list_ops.tensor_list_push_back(l, child_l)
with context.device("gpu:0"):
    l_gpu = array_ops.identity(l)
    _, child_l_gpu = list_ops.tensor_list_pop_back(
        l_gpu, element_dtype=dtypes.variant)
    self.assertAllEqual(
        self.evaluate(
            list_ops.tensor_list_pop_back(
                child_l_gpu, element_dtype=dtypes.float32)[1]), 2.0)
l_cpu = array_ops.identity(l_gpu)
_, child_l_cpu = list_ops.tensor_list_pop_back(
    l_cpu, element_dtype=dtypes.variant)
self.assertAllEqual(
    self.evaluate(
        list_ops.tensor_list_pop_back(
            child_l_cpu, element_dtype=dtypes.float32)[1]), 2.0)
